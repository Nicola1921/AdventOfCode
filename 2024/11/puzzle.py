import math
import os
import time
import unittest


def count_digits(num: int) -> int:
    return math.floor(math.log10(num) + 1)


def update_stones(stones: dict) -> dict:
    next_stones = dict()

    for stone in stones:
        if stone == 0:
            z_stone = 1
            next_stones[z_stone] = next_stones.get(z_stone, 0) + stones.get(stone, 0)
            continue

        digits = count_digits(stone)
        if digits % 2 == 0:
            l_stone = int(stone // 10 ** (digits / 2))
            r_stone = int(stone % 10 ** (digits / 2))

            next_stones[l_stone] = next_stones.get(l_stone, 0) + stones.get(stone, 0)
            next_stones[r_stone] = next_stones.get(r_stone, 0) + stones.get(stone, 0)
            continue

        m_stone = stone * 2024
        next_stones[m_stone] = next_stones.get(m_stone, 0) + stones.get(stone, 0)

    return next_stones


def solve(input_file_path: str, iterations: int) -> int:
    stones = dict()
    with open(input_file_path, "r") as file:
        for num in file.readline().split():
            stone = int(num)
            stones[stone] = stones.get(stone, 0) + 1

    # print(f"Iteration: 0; Stones: {stones}")
    for i in range(iterations):
        stones = update_stones(stones)
        # print(f"Iteration: {i + 1}; Stones: {stones} ")

    return sum(stones.values())


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
    print(f"Result Part1: {solve(input_file_path, 25)}")
    print(f"Duration: {round(time.time() - start_time, 4)} s")
    start_time = time.time()
    print(f"Result Part2: {solve(input_file_path, 75)}")
    print(f"Duration: {round(time.time() - start_time, 4)} s")
