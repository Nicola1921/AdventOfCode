import os
import re
import unittest
from functools import reduce
from operator import mul


def solve(input_file_path: str) -> tuple:
    sum_without_instructions = 0
    sum_with_instructions = 0

    with open(input_file_path, "r") as file:
        text = file.read()
        all_multiplications = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", text)

    do_calculate = True
    for multiplication in all_multiplications:
        if multiplication == "don't()":
            do_calculate = False
        elif multiplication == "do()":
            do_calculate = True
        else:
            factors = re.findall(r"\d+", multiplication)
            val = reduce(mul, map(int, factors))

            sum_without_instructions += val

            if do_calculate:
                sum_with_instructions += val

    return sum_without_instructions, sum_with_instructions


class Test(unittest.TestCase):
    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(solve(input_file_path)[0], 161)

        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData_Part2.txt"
        )

        self.assertEqual(solve(input_file_path)[1], 48)


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    print(f"Result: {solve(input_file_path)}")
