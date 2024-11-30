import os
import re
import unittest
from typing import List
from dataclasses import dataclass


@dataclass
class Round:
    red: int
    green: int
    blue: int


@dataclass
class Game:
    game_number: int
    rounds: List[Round]


max_values = Round(red=12, green=13, blue=14)


def map_to_round(str: str) -> Round:
    round = Round(0, 0, 0)

    for color in str.split(","):
        if "red" in color:
            round.red = int(re.search(r"\d+", color).group())
        if "green" in color:
            round.green = int(re.search(r"\d+", color).group())
        if "blue" in color:
            round.blue = int(re.search(r"\d+", color).group())

    return round


def map_to_game(line: str) -> Game:

    game_data = line.split(":")
    game_number = int(re.search(r"\d+", game_data[0]).group())
    rounds = list(map(map_to_round, game_data[1].split(";")))

    return Game(game_number=game_number, rounds=rounds)


def round_is_valid(round: Round) -> bool:
    if round.red > max_values.red:
        return False
    if round.green > max_values.green:
        return False
    if round.blue > max_values.blue:
        return False

    return True


def game_is_valid(game: Game) -> bool:
    for round in game.rounds:
        is_valid = round_is_valid(round)
        if not is_valid:
            return False

    return True


def sum_possible_games(filename):
    with open(filename, "r") as file:
        sum = 0
        for line in file:
            game = map_to_game(line)
            if game_is_valid(game):
                sum += game.game_number

        return sum


class Test(unittest.TestCase):
    def test_game_is_valid(self):

        self.assertTrue(
            game_is_valid(
                map_to_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
            )
        )
        self.assertTrue(
            game_is_valid(
                map_to_game(
                    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
                )
            )
        )
        self.assertFalse(
            game_is_valid(
                map_to_game(
                    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
                )
            )
        )
        self.assertFalse(
            game_is_valid(
                map_to_game(
                    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
                )
            )
        )
        self.assertTrue(
            game_is_valid(
                map_to_game("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
            )
        )


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    print(f"Result: {sum_possible_games(input_file_path)}")
