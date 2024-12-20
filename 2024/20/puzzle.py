import os
import time
import math

WALL = "#"
EMPTY = "."
START = "S"
END = "E"

ADJ_MATRIX = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def print_map(data_map: list):
    for row in data_map:
        for char in row:
            print_char = EMPTY
            if char == WALL:
                print_char = WALL
            elif char == START:
                print_char = START
            elif char == END:
                print_char = END

            print(print_char, end="")
        else:
            print()
    else:
        print()


def get_parse_input(input_file_path: str) -> tuple[list, list]:
    data_map = []
    with open(input_file_path, "r") as file:
        for line in file:
            data_map.append(list(line.rstrip()))

    return data_map


def walk(data_map: list) -> dict:
    end_pos = find_position(data_map, END)
    last_point = end_pos
    walked_points = {end_pos: 0}

    while data_map[last_point[0]][last_point[1]] != START:
        for x, y in ADJ_MATRIX:
            next_pos = (x + last_point[0], y + last_point[1])

            if (
                data_map[next_pos[0]][next_pos[1]] == EMPTY
                or data_map[next_pos[0]][next_pos[1]] == START
            ) and next_pos not in walked_points:
                costs = len(walked_points)
                walked_points[next_pos] = costs
                last_point = next_pos
                break

    return walked_points


def find_position(data_map: list, find: chr) -> tuple:
    return [
        (x, y)
        for x in range(len(data_map))
        for y, char in enumerate(data_map[x])
        if char == find
    ][0]


def get_reachable_points(n):
    reachable_points = []

    for row in range(-n, n + 1):
        for col in range(-n + abs(row), n - abs(row) + 1):
            if row != 0 or col != 0:
                num_cheats = abs(row) + abs(col)
                reachable_points.append([row, col, num_cheats])

    return reachable_points


def find_cheats(walk_data: dict, num_cheats: int) -> dict:
    cheats = dict()
    reachable_points = get_reachable_points(num_cheats)

    for pos, cost in walk_data.items():
        points_on_walk = [
            [(pos[0] + row, pos[1] + col), nc]
            for row, col, nc in reachable_points
            if (pos[0] + row, pos[1] + col) in walk_data
        ]

        for p, nc in points_on_walk:
            saved_time = cost - (walk_data.get(p) + nc)

            if saved_time > 0:
                cheats[saved_time] = cheats.get(saved_time, 0) + 1

    return cheats


def solve(input_file_path: str, num_cheats: int) -> int:
    data_map = get_parse_input(input_file_path)
    walk_data = walk(data_map)

    cheats = find_cheats(walk_data, num_cheats)
    # print(dict(sorted(cheats.items())))
    return sum([val for key, val in cheats.items() if key >= 100])


if __name__ == "__main__":
    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    start_time = time.time()
    print(f"Result Part1: {solve(input_file_path, 2)}")
    print(f"Duration: {round(time.time() - start_time, 4)} s")
    start_time = time.time()
    print(f"Result Part2: {solve(input_file_path, 20)}")
    print(f"Duration: {round(time.time() - start_time, 4)} s")
