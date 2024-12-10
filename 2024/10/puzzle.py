import os
import unittest

MOVEMENT = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def build_data_map(input_file_path: str) -> list:
    data_map = []
    with open(input_file_path, "r") as file:
        for line in file:
            data_map.append(list(map(int, list(line.rstrip()))))

    return data_map


def is_within_bounds(pos: tuple, max: tuple) -> bool:
    if pos[0] >= max[0] or pos[0] < 0:
        return False
    if pos[1] >= max[1] or pos[1] < 0:
        return False

    return True


def get_trail_heads(data_map: list, pos: tuple) -> set:
    trail_heads = set()
    current_value = data_map[pos[0]][pos[1]]

    print(f"Position: {pos}, Current Value: {current_value}")

    if current_value == 9:
        print(f"Position: {pos} is Trail-Head")
        return {pos}

    possible_next_steps = []

    for x, y in MOVEMENT:
        next_pos = (pos[0] + x, pos[1] + y)
        if not is_within_bounds(next_pos, (len(data_map), len(data_map[0]))):
            continue

        next_value = data_map[next_pos[0]][next_pos[1]]

        if next_value - 1 == current_value:
            possible_next_steps.append(next_pos)

    for next_step in possible_next_steps:
        trail_heads = trail_heads.union(get_trail_heads(data_map, next_step))

    return trail_heads


def solve(input_file_path: str) -> int:
    data_map = build_data_map(input_file_path)

    sum_trails = 0
    for row, _ in enumerate(data_map):
        for col, _ in enumerate(data_map):
            if data_map[row][col] == 0:
                trail_head = get_trail_heads(data_map, (row, col))
                sum_trails += len(trail_head)
                print("--------------Find next Start-Position----------------")

    return sum_trails


class Test(unittest.TestCase):
    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(solve(input_file_path), 36)


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    print(f"Result: {solve(input_file_path)}")
