import os
import unittest

ADJ_MATRIX = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

len_row = 0
len_col = 0


def create_word_search_array(input_file_path: str) -> list:
    word_search_array = []
    with open(input_file_path, "r") as file:
        for line in file:
            word_search_array.append(list(line.rstrip()))

    global len_row, len_col
    len_row = len(word_search_array)
    len_col = len(word_search_array[0])

    return word_search_array


def is_within_bounds(row: int, col: int) -> bool:
    if row >= len_row or row < 0:
        return False
    if col >= len_col or col < 0:
        return False

    return True


def is_char_at_position(char_to_check: chr, row: int, col: int, array: list) -> bool:
    if is_within_bounds(row, col) and array[row][col] == char_to_check:
        return True

    return False


def solve_part1(input_file_path: str) -> int:
    sum_xmas = 0
    word_search_array = create_word_search_array(input_file_path)
    for row, str in enumerate(word_search_array):
        for col, char in enumerate(str):
            if char != "X":
                continue
            for adj_field in ADJ_MATRIX:
                next_row = row + adj_field[0]
                next_col = col + adj_field[1]
                if not is_char_at_position("M", next_row, next_col, word_search_array):
                    continue

                next_row = next_row + adj_field[0]
                next_col = next_col + adj_field[1]
                if not is_char_at_position("A", next_row, next_col, word_search_array):
                    continue

                next_row = next_row + adj_field[0]
                next_col = next_col + adj_field[1]
                if is_char_at_position("S", next_row, next_col, word_search_array):
                    sum_xmas += 1

    return sum_xmas


class Test(unittest.TestCase):
    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(solve_part1(input_file_path), 18)


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    print(f"Result Part1: {solve_part1(input_file_path)}")
