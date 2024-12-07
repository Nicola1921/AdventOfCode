import os
import time
import unittest

GUARD_CHAR = "^"
WALL_CHAR = "#"
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def build_data_map(input_file_path: str) -> list:
    data_map = []
    with open(input_file_path, "r") as file:
        for line in file:
            data_map.append(list(line.rstrip()))

    return data_map


def find_guard_pos(data_map: list) -> tuple:
    return [
        (x, y)
        for x in range(len(data_map))
        for y, char in enumerate(data_map[x])
        if char == GUARD_CHAR
    ][0]


def change_direction(curr_idx: int) -> int:
    next_idx = curr_idx + 1
    if next_idx >= len(DIRECTIONS):
        next_idx = 0

    return next_idx


def is_within_bounds(pos: tuple, max: tuple) -> bool:
    if pos[0] >= max[0] or pos[0] < 0:
        return False
    if pos[1] >= max[1] or pos[1] < 0:
        return False

    return True


def is_loop(data_map: list, obstacle_pos: tuple) -> int:
    walked_points = set()
    max_bounds = (len(data_map), len(data_map[0]))
    guard_direction_idx = 0
    guard_pos = find_guard_pos(data_map)
    within_bounds = is_within_bounds(guard_pos, max_bounds)

    while within_bounds:
        entry = (guard_pos, guard_direction_idx)
        if entry in walked_points:
            return 1

        walked_points.add(entry)

        dir = DIRECTIONS[guard_direction_idx]
        next_pos = (guard_pos[0] + dir[0], guard_pos[1] + dir[1])
        within_bounds = is_within_bounds(next_pos, max_bounds)

        if not within_bounds:
            return 0

        if data_map[next_pos[0]][next_pos[1]] == WALL_CHAR or next_pos == obstacle_pos:
            guard_direction_idx = change_direction(guard_direction_idx)
        else:
            guard_pos = next_pos

    return 0


def guard_walk(data_map: list) -> None:
    walked_points = set()
    max_bounds = (len(data_map), len(data_map[0]))
    guard_direction_idx = 0
    guard_pos = find_guard_pos(data_map)
    within_bounds = is_within_bounds(guard_pos, max_bounds)

    while within_bounds:
        walked_points.add((guard_pos[0], guard_pos[1]))

        dir = DIRECTIONS[guard_direction_idx]
        next_pos = (guard_pos[0] + dir[0], guard_pos[1] + dir[1])
        within_bounds = is_within_bounds(next_pos, max_bounds)

        if not within_bounds:
            break

        if data_map[next_pos[0]][next_pos[1]] == WALL_CHAR:
            guard_direction_idx = change_direction(guard_direction_idx)
        else:
            guard_pos = next_pos

    return walked_points


def find_loops(data_map: list, walked_points: set) -> int:
    sum_loops = 0

    for obstacle in walked_points:
        sum_loops += is_loop(data_map, obstacle)

    return sum_loops


def solve(input_file_path: str) -> tuple:
    data_map = build_data_map(input_file_path)
    walked_points = guard_walk(data_map)

    sum_loops = find_loops(data_map, walked_points)

    return len(walked_points), sum_loops


class Test(unittest.TestCase):
    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(solve(input_file_path), (41, 6))


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    start_Time = time.time()
    print(f"Result: {solve(input_file_path)}")
    print(f"Duration: {round(time.time() - start_Time, 4)} s")
