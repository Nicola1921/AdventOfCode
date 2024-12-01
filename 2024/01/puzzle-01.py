import bisect
import os
import re
import time
import unittest


def solve(input_file_path: str) -> tuple[int]:
    left_list = []
    right_list = []

    with open(input_file_path, "r") as file:
        for line in file:
            numbers = re.findall(r"\d+", line)
            bisect.insort_left(left_list, int(numbers[0]))
            bisect.insort_left(right_list, int(numbers[1]))

    distance_list = list(map(lambda x, y: abs(x - y), left_list, right_list))
    distance_score = sum(distance_list)

    similarity_score = 0
    for entry in left_list:
        idx = bisect.bisect_left(right_list, entry)
        if idx >= len(right_list):
            continue

        while right_list[idx] == entry:
            similarity_score += entry
            idx += 1
            if idx >= len(right_list):
                break

    return distance_score, similarity_score


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
    start_time = time.time()
    print(
        f"Result: {solve(input_file_path)} (Time: {round((time.time() - start_time)*1000, 4)} ms)"
    )
