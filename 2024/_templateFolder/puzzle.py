import os
import time

input_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")


def parse_file() -> list:
    with open(input_file_path, "r") as file:
        data = file.read().splitlines()

    return data


def solve(data: list) -> int:

    return 0


if __name__ == "__main__":
    data = parse_file()

    print("-" * 10 + "PART 1" + "-" * 10)
    start_time = time.time()
    print(f"Result: {solve(data)}")
    print(f"Duration: {round(time.time() - start_time, 2)} s", end="\n\n")
