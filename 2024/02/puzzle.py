import os
import unittest

MIN_DIFF = 1
MAX_DIFF = 3


def solve(input_file_path: str) -> int:
    safe_reports = 0
    with open(input_file_path, "r") as file:
        for line in file:
            numbers = line.rsplit()
            numbers = list(map(int, numbers))

            safe_reports += 1 if is_report_safe(numbers) else 0
    return safe_reports


def is_report_safe(numbers):
    numbers_length = len(numbers)

    if numbers_length < 2:
        return False

    is_increasing = numbers[0] < numbers[1]

    for idx in range(numbers_length):
        if idx == numbers_length - 1:
            return True
        if numbers[idx] < numbers[idx + 1] and not is_increasing:
            return False
        if numbers[idx] > numbers[idx + 1] and is_increasing:
            return False

        abs_diff = abs(numbers[idx] - numbers[idx + 1])
        if abs_diff > MAX_DIFF or abs_diff < MIN_DIFF:
            return False

    return True


class Test(unittest.TestCase):
    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(solve(input_file_path), 2)


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    print(f"Result: {solve(input_file_path)}")
