import os
import re
import unittest


def solve(input_file_path: str) -> int:
    with open(input_file_path, "r") as file:
        sum = 0
        char_array = [list(line.rstrip()) for line in file]

        for r in range(len(char_array)):
            current_num = ""
            for c in range(len(char_array[r])):
                is_digit = char_array[r][c].isdigit()
                if c + 1 < len(char_array[r]):
                    next_is_digit = char_array[r][c + 1].isdigit()
                else:
                    next_is_digit = False

                if is_digit:
                    current_num += char_array[r][c]
                if is_digit and not next_is_digit:
                    for rc in range(max(0, r - 1), min(r + 2, len(char_array))):
                        for cc in range(
                            max(0, c - len(current_num)), min(c + 2, len(char_array[r]))
                        ):
                            if is_symbol(char_array[rc][cc]):
                                sum += int(current_num)
                                break
                        else:
                            continue
                        break

                    current_num = ""

        return sum


def is_symbol(char: str):
    if char.isdigit() or char == ".":
        return False

    return True


class Test(unittest.TestCase):
    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(solve(input_file_path), 4361)


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    print(f"Result Part1: {solve(input_file_path)}")
