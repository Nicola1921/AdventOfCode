import os
import re
import unittest

numbersDict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def calc_calibration(filename: str) -> int:
    with open(filename, "r") as file:
        sum = 0
        for line in file:
            sum += get_calibration_value(line)
        return sum


def get_calibration_value(line: str) -> int:
    numbers = [None] * len(line)
    for key, value in numbersDict.items():
        for sub in re.finditer(key, line):
            numbers[sub.start()] = value

        for sub in re.finditer(value, line):
            numbers[sub.start()] = value

    numbers = [x for x in numbers if x is not None]

    if len(numbers) > 1:
        return int(numbers[0] + numbers[-1])
    elif len(numbers) == 1:
        return int(numbers[0] * 2)
    else:
        return 0


class Test(unittest.TestCase):
    def test_get_calibration_value(self):
        self.assertEqual(get_calibration_value("3test3t5est"), 35)
        self.assertEqual(get_calibration_value("ref4asd"), 44)
        self.assertEqual(get_calibration_value("sadasd"), 0)
        self.assertEqual(get_calibration_value(("xxtwoxxninexx")), 29)
        self.assertEqual(get_calibration_value(("two1nine")), 29)
        self.assertEqual(get_calibration_value(("eightwothree")), 83)
        self.assertEqual(get_calibration_value(("abcone2threexyz")), 13)
        self.assertEqual(get_calibration_value(("xtwone3four")), 24)
        self.assertEqual(get_calibration_value(("4nineeightseven2")), 42)
        self.assertEqual(get_calibration_value(("zoneight234")), 14)
        self.assertEqual(get_calibration_value(("7pqrstsixteen")), 76)


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    print(f"Result: {calc_calibration(input_file_path)}")
