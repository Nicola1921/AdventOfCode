import os
import unittest

ADJ_MATRIX = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIAG_ADJ_MATRIX = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
MAX_FENCES = 4


def is_within_bounds(pos: tuple, max_size: tuple) -> bool:
    if pos[0] >= max_size[0] or pos[0] < 0:
        return False
    if pos[1] >= max_size[1] or pos[1] < 0:
        return False

    return True


def find_adj_points(data_map: list, pos: tuple) -> int:
    current_val = data_map[pos[0]][pos[1]]

    adj_points = []
    for x, y in ADJ_MATRIX:
        adj_pos = (x + pos[0], y + pos[1])

        if not is_within_bounds(adj_pos, (len(data_map), len(data_map[0]))):
            continue

        if data_map[adj_pos[0]][adj_pos[1]] == current_val:
            adj_points.append(adj_pos)

    return adj_points


def calculate_corners(point: tuple, points: set) -> int:
    neighbours = []
    for x, y in ADJ_MATRIX:
        if (x + point[0], y + point[1]) in points:
            neighbours.append((x + point[0], y + point[1]))

    corners = 0
    match len(neighbours):
        case 0:
            corners = 4
        case 1:
            corners = 2
        case 2:
            if (
                neighbours[0][0] != neighbours[1][0]
                and neighbours[0][1] != neighbours[1][1]
            ):
                corners = 1

    for x, y in DIAG_ADJ_MATRIX:
        if (
            (x + point[0], y + point[1]) not in points
            and (point[0], y + point[1]) in points
            and (x + point[0], point[1]) in points
        ):
            corners += 1

    return corners


def calculate_sides(points: set) -> int:
    corners = 0

    for point in points:
        corners += calculate_corners(point, points)

    return corners


def resolve_cluster(
    data_map: list, pos: tuple, resolved_points: set
) -> set[tuple[int, int]]:

    resolved_points.add(pos)
    adj_points = find_adj_points(data_map, pos)

    for adj_pos in [ap for ap in adj_points if ap not in resolved_points]:
        resolved_points = resolved_points.union(
            resolve_cluster(data_map, adj_pos, resolved_points)
        )

    return resolved_points


def solve(input_file_path: str) -> int:
    data_map = []
    with open(input_file_path, "r") as file:
        for line in file:
            data_map.append(list(line.rstrip()))

    data = []
    resolved_points = set()
    for idx_row, row in enumerate(data_map):
        for idx_col, char in enumerate(row):
            if (idx_row, idx_col) not in resolved_points:
                points = resolve_cluster(data_map, (idx_row, idx_col), set())
                resolved_points = resolved_points.union(points)
                sides_length = calculate_sides(points)

                # print(
                #     f"{char}: Area: {len(points)}, Sides: {sides_length}, P: {points}"
                # )
                data.append(sides_length * len(points))

    return sum(data)


class Test(unittest.TestCase):
    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(solve(input_file_path), 1206)


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    print(f"Result: {solve(input_file_path)}")
