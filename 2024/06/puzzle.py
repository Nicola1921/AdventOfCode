import os
import unittest

GUARD_CHAR = "^"
WALKED_CHAR = "X"
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


def guard_walk(data_map: list) -> list:
    max_bounds = (len(data_map), len(data_map[0]))
    guard_direction_idx = 0
    guard_pos = find_guard_pos(data_map)
    within_bounds = is_within_bounds(guard_pos, max_bounds)

    while within_bounds:
        data_map[guard_pos[0]][guard_pos[1]] = WALKED_CHAR

        dir = DIRECTIONS[guard_direction_idx]
        next_pos = (guard_pos[0] + dir[0], guard_pos[1] + dir[1])
        within_bounds = is_within_bounds(next_pos, max_bounds)

        if not within_bounds:
            break

        if data_map[next_pos[0]][next_pos[1]] == WALL_CHAR:
            guard_direction_idx = change_direction(guard_direction_idx)
        else:
            guard_pos = next_pos

    return data_map


def print_map(map: list) -> None:
    for row in map:
        print(row)


def solve(input_file_path: str) -> int:
    data_map = build_data_map(input_file_path)
    walked_map = guard_walk(data_map)
    # print_map(walked_map)
    sum_walked = sum(row.count(WALKED_CHAR) for row in walked_map)

    return sum_walked


class Test(unittest.TestCase):
    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(solve(input_file_path), 41)


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    print(f"Result: {solve(input_file_path)}")
