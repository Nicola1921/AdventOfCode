import math
import os
import time
import unittest


def count_digits(num: int) -> int:
    return math.floor(math.log10(num) + 1)


def update_stones(stones: list) -> list:
    next_stones = []
    for stone in stones:
        if stone == 0:
            next_stones.append(1)
            continue

        digits = count_digits(stone)
        if digits % 2 == 0:

            next_stones.append(int(stone // 10 ** (digits / 2)))
            next_stones.append(int(stone % 10 ** (digits / 2)))
            continue

        next_stones.append(stone * 2024)

    return next_stones


def solve(input_file_path: str, iterations: int) -> int:
    stones = []
    with open(input_file_path, "r") as file:
        stones = list(map(int, file.readline().split()))

    # print(f"Iteration: 0; Stones: {stones}")
    for i in range(iterations):
        stones = update_stones(stones)
        print(f"Iteration: {i + 1}; Stones: ")

    return len(stones)


class Test(unittest.TestCase):
    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(solve(input_file_path, 6), 22)
        self.assertEqual(solve(input_file_path, 25), 55312)


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    start_time = time.time()
    print(f"Result: {solve(input_file_path, 25)}")
    print(f"Duration: {round(time.time() - start_time, 4)} s")
