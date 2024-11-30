import os
import re
import unittest

from functools import reduce

adj_matrix = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def solve(input_file_path: str) -> tuple:
    with open(input_file_path, "r") as file:
        numbers_coords = []
        symbols_coords = []

        char_matrix = [list(line.rstrip()) for line in file]

        num_rows = len(char_matrix)
        num_cols = len(char_matrix[0])

        for r in range(num_rows):
            number = []
            for c in range(num_cols):
                if char_matrix[r][c].isdigit():
                    number.append((r, c))
                elif len(number) > 0:
                    numbers_coords.append(
                        (number, int("".join(char_matrix[x][y] for x, y in number)))
                    )
                    number = []

                if is_symbol(char_matrix[r][c]):
                    symbols_coords.append((r, c))
            else:
                if len(number) > 0:
                    numbers_coords.append(
                        (number, int("".join(char_matrix[x][y] for x, y in number)))
                    )
                    number = []

        symbol_numbers = []
        for coords, num in numbers_coords:
            for coord in coords:
                is_adj = is_symbol_adjacent(coord, symbols_coords)
                if is_adj:
                    symbol_numbers.append(num)
                    break

        gear_numbers = []
        gear_coords = [(x, y) for x, y in symbols_coords if char_matrix[x][y] == "*"]
        for coords in gear_coords:
            adj_numbers = get_adj_numbers(coords, numbers_coords)
            if len(adj_numbers) == 2:
                gear_numbers.append(reduce(lambda x, y: x * y, adj_numbers))

        return sum(symbol_numbers), sum(gear_numbers)


def is_symbol_adjacent(coord: tuple, symbols_coords: list[tuple]) -> bool:
    for dx, dy in adj_matrix:
        if (coord[0] + dx, coord[1] + dy) in symbols_coords:
            return True

    return False


def get_adj_numbers(coord: tuple, numbers: list[tuple]) -> list[int]:
    adj_numbers = []
    for coords, num in numbers:
        if any((coord[0] + dx, coord[1] + dy) in coords for dx, dy in adj_matrix):
            adj_numbers.append(num)

    return adj_numbers


def is_symbol(char: str):
    if char.isdigit() or char == ".":
        return False

    return True


class Test(unittest.TestCase):
    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(solve(input_file_path), (4361, 467835))


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    print(f"Result: {solve(input_file_path)}")
