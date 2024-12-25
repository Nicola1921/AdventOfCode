import os
import time
from heapq import heappop, heappush
from itertools import chain

INPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")

WALL = "#"
EMPTY = "."
START = "S"
END = "E"

EAST = (0, 1)
WEST = (0, -1)
NORTH = (-1, 0)
SOUTH = (1, 0)
DIRECTIONS = [EAST, SOUTH, WEST, NORTH]


def parse_file() -> list:
    data_map = []
    with open(INPUT, "r") as file:
        for line in file:
            data_map.append(list(line.rstrip()))

    return data_map


def find_position(data_map: list, find: chr) -> tuple:
    return [
        (x, y)
        for x in range(len(data_map))
        for y, char in enumerate(data_map[x])
        if char == find
    ][0]


def get_char(data_map: list, pos: tuple) -> chr:
    return data_map[pos[0]][pos[1]]


def solve() -> int:
    data_map = parse_file()

    seen = dict()
    start_pos = find_position(data_map, START)
    heap = [(0, 0, start_pos, [start_pos])]

    best_value = float("inf")
    all_paths = []

    while heap:
        points, dir_idx, pos, path = heappop(heap)
        if points > best_value:
            continue

        if data_map[pos[0]][pos[1]] == END:
            all_paths.append(path)
            if points < best_value:
                best_value = points

        if (dir_idx, pos) in seen and seen.get((dir_idx, pos)) < points:
            continue

        seen[(dir_idx, pos)] = points

        next_pos = (
            pos[0] + DIRECTIONS[dir_idx][0],
            pos[1] + DIRECTIONS[dir_idx][1],
        )

        if (
            data_map[next_pos[0]][next_pos[1]] in {EMPTY, END}
            and (dir_idx, next_pos) not in seen
        ):
            heappush(heap, (points + 1, dir_idx, next_pos, path + [next_pos]))

        if (n_dir_idx := (dir_idx - 1) % 4, pos) not in seen:
            heappush(heap, (points + 1000, n_dir_idx, pos, path))

        if (n_dir_idx := (dir_idx + 1) % 4, pos) not in seen:
            heappush(heap, (points + 1000, n_dir_idx, pos, path))

    return best_value, len(set(chain.from_iterable(all_paths)))


if __name__ == "__main__":

    print("-" * 10 + "PART 1 & 2" + "-" * 10)
    start_time = time.time()
    print(f"Result: {solve()}")
    print(f"Duration: {round(time.time() - start_time, 2)} s", end="\n\n")
