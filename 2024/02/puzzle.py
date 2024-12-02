import os
import unittest

MIN_DIFF = 1
MAX_DIFF = 3


def solve(input_file_path: str) -> tuple[int]:
    safe_reports = 0
    safe_reports_damped = 0
    with open(input_file_path, "r") as file:
        for line in file:
            report_numbers = line.rsplit()
            report_numbers = list(map(int, report_numbers))

            safe_reports += 1 if is_report_safe(report_numbers) else 0
            safe_reports_damped += 1 if is_damped_report_safe(report_numbers) else 0

    return safe_reports, safe_reports_damped


def is_report_safe(report_numbers: list[int]) -> bool:
    numbers_length = len(report_numbers)

    if numbers_length < 2:
        return False

    is_increasing = report_numbers[0] < report_numbers[1]

    for idx in range(numbers_length):
        if idx == numbers_length - 1:
            return True
        if report_numbers[idx] < report_numbers[idx + 1] and not is_increasing:
            return False
        if report_numbers[idx] > report_numbers[idx + 1] and is_increasing:
            return False

        abs_diff = abs(report_numbers[idx] - report_numbers[idx + 1])
        if abs_diff > MAX_DIFF or abs_diff < MIN_DIFF:
            return False

    return True


def is_damped_report_safe(report_numbers: list[int]) -> bool:
    if is_report_safe(report_numbers):
        return True

    for idx in range(len(report_numbers)):
        damped_report_numbers = report_numbers[:idx] + report_numbers[idx + 1 :]
        if is_report_safe(damped_report_numbers):
            return True


class Test(unittest.TestCase):
    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(solve(input_file_path), (2, 4))


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    print(f"Result: {solve(input_file_path)}")
