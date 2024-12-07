import os
import re
import unittest


def parse_equations(input_file_path: str) -> list:
    equations = []
    with open(input_file_path, "r") as file:
        for line in file:
            equation = line.split(":")
            values = list(map(int, re.findall(r"\d+", equation[1])))

            equations.append((int(equation[0]), values))

    return equations


def is_valid_equation(equation_result: int, equation_values: list[int]) -> bool:

    if len(equation_values) == 1:
        return equation_values[0] == equation_result

    next_calc_add = equation_values[0] + equation_values[1]
    next_calc_mul = equation_values[0] * equation_values[1]

    if len(equation_values) == 2:
        return next_calc_add == equation_result or next_calc_mul == equation_result

    if is_valid_equation(equation_result, [next_calc_add] + equation_values[2:]):
        return True

    if is_valid_equation(equation_result, [next_calc_mul] + equation_values[2:]):
        return True

    return False


def solve(input_file_path: str) -> int:
    total_calibration_result = 0
    equations = parse_equations(input_file_path)

    for equation_result, equation_values in equations:
        if is_valid_equation(equation_result, equation_values):
            total_calibration_result += equation_result

    return total_calibration_result


class Test(unittest.TestCase):
    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(solve(input_file_path), 3749)


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    print(f"Result: {solve(input_file_path)}")
