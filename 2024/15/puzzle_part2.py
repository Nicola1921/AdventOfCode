import os
import unittest

WALL = "#"
BOX = "O"
BIG_BOX_START = "["
BIG_BOX_END = "]"
ROBOT = "@"
EMPTY = "."
UP = ("^", (-1, 0))
LEFT = ("<", (0, -1))
RIGHT = (">", (0, 1))
DOWN = ("v", (1, 0))


def print_map(data_map: list):
    for row in range(len(data_map)):
        print(data_map[row])
    else:
        print()


def get_parse_input(input_file_path: str) -> tuple[list, list]:
    data_map = []
    instructions = []
    with open(input_file_path, "r") as file:
        content = file.read()
        content = content.split("\n\n")
        for line in content[0].split("\n"):
            data_line = []
            for char in line:
                if char == BOX:
                    data_line.append(BIG_BOX_START)
                    data_line.append(BIG_BOX_END)
                    continue
                if char == ROBOT:
                    data_line.append(ROBOT)
                    data_line.append(EMPTY)
                    continue

                data_line.append(char)
                data_line.append(char)
            else:
                data_map.append(data_line)

        instructions = list(content[1].rstrip())

    return data_map, instructions


def calc_distance(box: tuple) -> int:
    return box[0] * 100 + box[1]


def find_positions(data_map: list, find: chr) -> list:
    return [
        (x, y)
        for x in range(len(data_map))
        for y, char in enumerate(data_map[x])
        if char == find
    ]


def check_movement(data_map: list, robot_pos: tuple, dir: tuple) -> tuple[bool, set]:
    can_move = False
    boxes_to_move = set()

    check_pos = (robot_pos[0] + dir[0], robot_pos[1] + dir[1])
    while data_map[check_pos[0]][check_pos[1]] != WALL:
        char = data_map[check_pos[0]][check_pos[1]]

        if char == EMPTY:
            can_move = True
            break

        if char == BIG_BOX_START:
            box_end_pos = (check_pos[0], check_pos[1] + 1)
            box = (check_pos, box_end_pos)

            if dir == UP[1] or dir == DOWN[1]:
                cm, bm = check_movement(data_map, box_end_pos, dir)
                if not cm:
                    break

                boxes_to_move = boxes_to_move.union(bm)

            boxes_to_move.add(box)

        elif char == BIG_BOX_END:
            box_start_pos = (check_pos[0], check_pos[1] - 1)
            box = (box_start_pos, check_pos)

            if dir == UP[1] or dir == DOWN[1]:
                cm, bm = check_movement(data_map, box_start_pos, dir)
                if not cm:
                    break

                boxes_to_move = boxes_to_move.union(bm)

            boxes_to_move.add(box)

        check_pos = (check_pos[0] + dir[0], check_pos[1] + dir[1])

    return can_move, boxes_to_move


def simulate_instruction(data_map: list, instruction: chr) -> list:
    robot_pos = find_positions(data_map, ROBOT)[0]
    dir = (0, 0)
    if instruction == UP[0]:
        dir = UP[1]
    elif instruction == LEFT[0]:
        dir = LEFT[1]
    elif instruction == RIGHT[0]:
        dir = RIGHT[1]
    elif instruction == DOWN[0]:
        dir = DOWN[1]
    else:
        return data_map

    can_move, boxes_to_move = check_movement(data_map, robot_pos, dir)

    if can_move:
        data_map[robot_pos[0]][robot_pos[1]] = EMPTY

        for box in boxes_to_move:
            data_map[box[0][0]][box[0][1]] = EMPTY
            data_map[box[1][0]][box[1][1]] = EMPTY

        for box in boxes_to_move:
            data_map[box[0][0] + dir[0]][box[0][1] + dir[1]] = BIG_BOX_START
            data_map[box[1][0] + dir[0]][box[1][1] + dir[1]] = BIG_BOX_END

        data_map[robot_pos[0] + dir[0]][robot_pos[1] + dir[1]] = ROBOT

    return data_map


def solve(input_file_path: str) -> int:
    data_map, instructions = get_parse_input(input_file_path)

    # print(f"Initial State")
    # print_map(data_map)

    for instruction in instructions:
        data_map = simulate_instruction(data_map, instruction)
        # print(f"Move {instruction}")
        # print_map(data_map)

    boxes = find_positions(data_map, BIG_BOX_START)
    sum_gps = sum(map(calc_distance, boxes))
    return sum_gps


class Test(unittest.TestCase):
    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(solve(input_file_path), 9021)


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    print(f"Result: {solve(input_file_path)}")
