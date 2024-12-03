import os
import re
import unittest
from functools import reduce
from operator import mul


def solve(input_file_path: str) -> int:
    with open(input_file_path, "r") as file:
        text = file.read()
        all_multiplications = re.findall(r"mul\(\d+,\d+\)", text)

    sum = 0
    for multiplication in all_multiplications:
        factors = re.findall(r"\d+", multiplication)
        sum += reduce(mul, map(int, factors))

    return sum


class Test(unittest.TestCase):
    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(solve(input_file_path), 161)


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    print(f"Result: {solve(input_file_path)}")
