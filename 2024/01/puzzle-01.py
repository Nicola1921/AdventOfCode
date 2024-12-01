import os
import re
import unittest

import numpy as np


def solve(input_file_path: str) -> tuple[int]:
    left_list = []
    right_list = []

    with open(input_file_path, "r") as file:
        for line in file:
            numbers = re.findall(r"\d+", line)
            left_list.append(int(numbers[0]))
            right_list.append(int(numbers[1]))

    left_list.sort()
    right_list.sort()

    distance_list = list(map(lambda x, y: abs(x - y), left_list, right_list))

    right_as_np_array = np.array(right_list)
    similarity_score = []
    for entry in left_list:
        occurences = np.where(right_as_np_array == entry)[0].size
        similarity_score.append(entry * occurences)

    return sum(distance_list), sum(similarity_score)


class Test(unittest.TestCase):
    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(solve(input_file_path), (11, 31))


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    print(f"Result: {solve(input_file_path)}")
