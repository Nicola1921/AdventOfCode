import os
import time

import numpy as np

input_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")


def mix_secret(num1: int, num2: int) -> int:
    return num1 ^ num2


def prune_secret(num: int) -> int:
    return num & (1 << 24) - 1


def calculate_next_secret(number: int) -> int:
    step1 = prune_secret(mix_secret(number, number << 6))  # *64
    step2 = prune_secret(mix_secret(step1, step1 >> 5))  # /32
    step3 = prune_secret(mix_secret(step2, step2 << 11))  # *2048

    return step3


def solve(depth: int) -> int:
    initial_numbers = np.loadtxt(input_file_path, dtype=int)

    secrets = []
    for num in initial_numbers:
        temp = num
        for _ in range(depth):
            temp = calculate_next_secret(temp)

        secrets.append(temp)

    return sum(secrets)


if __name__ == "__main__":
    print("-" * 10 + "PART 1" + "-" * 10)
    start_time = time.time()
    print(f"Result: {solve(2000)}")
    print(f"Duration: {round(time.time() - start_time, 2)} s", end="\n\n")
