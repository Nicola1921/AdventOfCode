import os
import time

INPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")


def parse_file() -> list:
    keys = []
    locks = []
    with open(INPUT, "r") as file:
        for lk in [block.split() for block in file.read().split("\n\n")]:
            height_map = []

            for col in range(len(lk[0])):
                col_height = sum([1 for row in range(len(lk)) if lk[row][col] == "#"])
                height_map.append(col_height)

            if lk[0].startswith("#"):
                locks.append(height_map)
            else:
                keys.append(height_map)

    return keys, locks


def solve() -> int:
    keys, locks = parse_file()

    num_pairs = 0
    for key in keys:
        num_pairs += sum(
            [all([x + y <= 7 for x, y in zip(key, lock)]) for lock in locks]
        )

    return num_pairs


if __name__ == "__main__":

    print("-" * 10 + "PART 1" + "-" * 10)
    start_time = time.time()
    print(f"Result: {solve()}")
    print(f"Duration: {round(time.time() - start_time, 2)} s", end="\n\n")
