import os
import re
import time
from collections import deque

EMPTY = "."
CORRUPTED = "#"
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

input_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")


def print_map(data_map: list):
    for row in data_map:
        for char in row:
            print(char, end="")
        else:
            print()
    else:
        print()


def parse_file() -> list:
    with open(input_file_path, "r") as file:
        # X is Distance to Left (COL); Y is Distance to Top (ROW)
        data = [tuple(map(int, pos)) for pos in re.findall(r"(\d+),(\d+)", file.read())]

    return data


def walk(grid: list, start_pos: tuple, end_pos: tuple, visited: set) -> int:
    queue = deque([(start_pos, 0)])
    visited.add(start_pos)

    while queue:
        pos, distance = queue.popleft()

        if pos == end_pos:
            return distance

        for dx, dy in DIRECTIONS:
            next_pos = (pos[0] + dx, pos[1] + dy)

            if 0 <= next_pos[1] <= end_pos[1] and 0 <= next_pos[0] <= end_pos[0]:
                if grid[next_pos[1]][next_pos[0]] == EMPTY and next_pos not in visited:
                    visited.add(next_pos)
                    # grid[next_pos[1]][next_pos[0]] = "O"
                    queue.append((next_pos, distance + 1))

        # print_map(grid)

    return -1


def solve(bytes: int, grid_size: int) -> int:
    grid = [[EMPTY for _ in range(grid_size + 1)] for _ in range(grid_size + 1)]
    positions = parse_file()
    corrupted_pos = positions[:bytes]

    for pos in positions[bytes:]:
        corrupted_pos.append(pos)
        if walk(grid, (0, 0), (grid_size, grid_size), set(corrupted_pos)) == -1:
            return pos


if __name__ == "__main__":
    print("-" * 10 + "PART 2" + "-" * 10)
    start_time = time.time()
    print(f"Result: {solve(1024, 70)}")
    print(f"Duration: {round(time.time() - start_time, 2)} s", end="\n\n")
