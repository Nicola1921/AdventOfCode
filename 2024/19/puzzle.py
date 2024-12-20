import os
import unittest
from functools import cache

input_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")
towels = []


def parse_data(input_file_path: str) -> tuple[list[str], list[str]]:
    with open(input_file_path, "r") as file:
        towels, _, *combinations = file.read().splitlines()
        towels = [item.strip() for item in towels.split(",")]

    return towels, combinations


@cache
def is_possible_combination(str: str) -> bool:
    res = []
    prefixes = [t for t in towels if str.startswith(t)]
    for prefix in prefixes:
        res.append(is_possible_combination(str.removeprefix(prefix)))

    return str == "" or any(res)


if __name__ == "__main__":
    towels, combinations = parse_data(input_file_path)
    print(f"Result: {sum(map(is_possible_combination, combinations))}")
