import os
import time

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


def walk(data_map: list) -> list:
    start_pos = find_position(data_map, START)
    walked_points = [start_pos]

    while data_map[walked_points[-1][0]][walked_points[-1][1]] != END:
        for x, y in ADJ_MATRIX:
            next_pos = (x + walked_points[-1][0], y + walked_points[-1][1])

            if (
                data_map[next_pos[0]][next_pos[1]] == EMPTY
                or data_map[next_pos[0]][next_pos[1]] == END
            ) and next_pos not in walked_points:
                walked_points.append(next_pos)
                break

    return walked_points


def find_position(data_map: list, find: chr) -> tuple:
    return [
        (x, y)
        for x in range(len(data_map))
        for y, char in enumerate(data_map[x])
        if char == find
    ][0]


def find_cheats(walk_data: list) -> dict:
    cheats = dict()

    for idx, pos in enumerate(walk_data):
        for dx, dy in ADJ_MATRIX:
            if (pos[0] + dx, pos[1] + dy) not in walk_data and (
                pos[0] + 2 * dx,
                pos[1] + 2 * dy,
            ) in walk_data:
                shortcut_idx = walk_data.index((pos[0] + 2 * dx, pos[1] + 2 * dy))
                if shortcut_idx > idx:
                    saved_time = shortcut_idx - idx - 2
                    cheats[saved_time] = cheats.get(saved_time, 0) + 1

    return cheats


def solve(input_file_path: str) -> int:
    data_map = get_parse_input(input_file_path)
    walk_data = walk(data_map)

    cheats = find_cheats(walk_data)

    # print_map(data_map)
    # print(len(walk_data) - 1)
    # print(cheats)

    return sum([val for key, val in cheats.items() if key >= 100])


if __name__ == "__main__":
    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    start_time = time.time()
    print(f"Result: {solve(input_file_path)}")
    print(f"Duration: {round(time.time() - start_time, 4)} s")
