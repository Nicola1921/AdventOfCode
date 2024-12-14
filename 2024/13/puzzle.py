import os
import re
import unittest

import numpy as np

TOKEN_COST_A = 3
TOKEN_COST_B = 1


def map_input(input_file_path: str) -> list:
    with open(input_file_path, "r") as file:
        data = re.findall(
            r"(\d+).*?(\d+).*?\s.*?(\d+).*?(\d+).*?\s.*?(\d+).*?(\d+)",
            file.read(),
        )
        return data


def solve(input_file_path: str, prize_offset: int) -> int:
    data = map_input(input_file_path)

    sum = 0
    for machine in data:
        ax, ay, bx, by, rx, ry = map(int, machine)
        res = np.round(
            np.linalg.solve(
                np.array([[ax, bx], [ay, by]]),
                np.array([rx + prize_offset, ry + prize_offset]),
            )
        )

        if np.array_equal(
            np.array([res[0] * ax + res[1] * bx, res[0] * ay + res[1] * by]),
            np.array([rx + prize_offset, ry + prize_offset]),
        ):
            sum += np.dot(res, [3, 1])
        else:
            sum += 0

    return int(sum)


class Test(unittest.TestCase):
    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(solve(input_file_path, 0), 480)


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    print(f"Result Part 1: {solve(input_file_path, 0)}")
    print(f"Result Part 2: {solve(input_file_path, 1e13)}")
