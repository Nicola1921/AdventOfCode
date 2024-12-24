import os
import time

INPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")


def parse_file() -> list:
    with open(INPUT, "r") as file:
        data = file.read().splitlines()

    return data


def solve() -> int:
    data = parse_file()

    return 0


if __name__ == "__main__":

    print("-" * 10 + "PART 1" + "-" * 10)
    start_time = time.time()
    print(f"Result: {solve()}")
    print(f"Duration: {round(time.time() - start_time, 2)} s", end="\n\n")
