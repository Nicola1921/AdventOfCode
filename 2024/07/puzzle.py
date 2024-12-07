import math
import os
import re
import time
import unittest
from enum import Enum
from itertools import product


class Operator(Enum):
    SUM = "+"
    MUL = "*"
    CONCAT = "||"


def parse_equations(input_file_path: str) -> list:
    equations = []
    with open(input_file_path, "r") as file:
        for line in file:
            equation = line.split(":")
            values = list(map(int, re.findall(r"\d+", equation[1])))

            equations.append((int(equation[0]), values))

    return equations


def calculate(equation_values: list[int], operators: list[chr]):
    sum = equation_values[0]

    for idx in range(len(operators)):
        if operators[idx] == Operator.SUM.value:
            sum += equation_values[idx + 1]
        if operators[idx] == Operator.MUL.value:
            sum *= equation_values[idx + 1]
        if operators[idx] == Operator.CONCAT.value:
            num = equation_values[idx + 1]
            sum = sum * pow(10, math.floor(math.log10(num) + 1)) + num
    return sum


def is_valid_equation(
    equation_result: int, equation_values: list[int], useable_operators: list
) -> bool:

    possible_operator_orders = product(
        useable_operators, repeat=(len(equation_values) - 1)
    )

    for operator_order in possible_operator_orders:
        if equation_result == calculate(list(equation_values), list(operator_order)):
            return True

    return False


def solve(input_file_path: str, useable_operators: list) -> int:
    total_calibration_result = 0
    equations = parse_equations(input_file_path)

    for equation_result, equation_values in equations:
        if is_valid_equation(equation_result, equation_values, useable_operators):
            total_calibration_result += equation_result

    return total_calibration_result


class Test(unittest.TestCase):
    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(
            solve(input_file_path, [Operator.SUM.value, Operator.MUL.value]), 3749
        )

    def test_solve_part2(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(
            solve(
                input_file_path,
                [Operator.SUM.value, Operator.MUL.value, Operator.CONCAT.value],
            ),
            11387,
        )


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    start_Time = time.time()
    print(
        f"Result Part1: {solve(input_file_path, [Operator.SUM.value, Operator.MUL.value])}"
    )
    print(f"Duration: {round(time.time() - start_Time, 4)} s")

    start_Time = time.time()
    print(
        f"Result Part2: {solve(input_file_path, [Operator.SUM.value, Operator.MUL.value, Operator.CONCAT.value])}"
    )
    print(f"Duration: {round(time.time() - start_Time, 4)} s")
