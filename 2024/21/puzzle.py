import os
import time
from functools import lru_cache

input_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")


def parse_file() -> list:
    with open(input_file_path, "r") as file:
        data = [list(d) for d in file.read().splitlines()]

    return data


def extract_num(input: list) -> int:
    return int("".join([i for i in input if i.isdigit()]))


def get_keypad_pos(char: str) -> tuple:
    match char:
        case "^":
            return (0, 1)
        case "A":
            return (0, 2)
        case "<":
            return (1, 0)
        case "v":
            return (1, 1)
        case ">":
            return (1, 2)


def get_numpad_pos(char: str) -> tuple:
    match char:
        case "7":
            return (0, 0)
        case "8":
            return (0, 1)
        case "9":
            return (0, 2)
        case "4":
            return (1, 0)
        case "5":
            return (1, 1)
        case "6":
            return (1, 2)
        case "1":
            return (2, 0)
        case "2":
            return (2, 1)
        case "3":
            return (2, 2)
        case "0":
            return (3, 1)
        case "A":
            return (3, 2)


@lru_cache(100)
def write_path(current_pos: tuple, pos: tuple, forbiden_pos: tuple) -> list:

    dx = pos[0] - current_pos[0]
    dy = pos[1] - current_pos[1]

    moves_row = "v" * abs(dx) if dx >= 0 else "^" * abs(dx)
    moves_col = ">" * abs(dy) if dy >= 0 else "<" * abs(dy)

    if len(moves_row) == len(moves_col) == 0:
        return ["A"]
    if len(moves_row) == 0:
        return [moves_col + "A"]
    if len(moves_col) == 0:
        return [moves_row + "A"]
    if (current_pos[0], pos[1]) == forbiden_pos:
        return [moves_row + moves_col + "A"]
    if (pos[0], current_pos[1]) == forbiden_pos:
        return [moves_col + moves_row + "A"]

    return [moves_row + moves_col + "A", moves_col + moves_row + "A"]


@lru_cache(100)
def keypad_inputs(input: list, depth: int) -> list:
    cx, cy = (0, 2)
    result = 0

    if depth == 0:
        return len(input)

    for move in input:
        x, y = get_keypad_pos(move)
        paths = write_path((cx, cy), (x, y), (0, 0))
        cx, cy = x, y

        result += min([keypad_inputs(p, depth - 1) for p in paths])

    return result


def numpad_inputs(input: list, depth: int = 1) -> list:
    cx, cy = (3, 2)
    result = 0

    for move in input:
        x, y = get_numpad_pos(move)
        paths = write_path((cx, cy), (x, y), (3, 0))
        cx, cy = x, y

        result += min([keypad_inputs(p, depth) for p in paths])

    return result


def solve(num_robots: int) -> int:
    sum = 0
    data = parse_file()

    for d in data:
        res = numpad_inputs(d, num_robots)
        sum += res * extract_num(d)

    return sum


if __name__ == "__main__":

    print("-" * 10 + "PART 1" + "-" * 10)
    start_time = time.time()
    print(f"Result: {solve(2)}")
    print(f"Duration: {round(time.time() - start_time, 4)} s", end="\n\n")

    print("-" * 10 + "PART 2" + "-" * 10)
    start_time = time.time()
    print(f"Result: {solve(25)}")
    print(f"Duration: {round(time.time() - start_time, 4)} s", end="\n\n")
