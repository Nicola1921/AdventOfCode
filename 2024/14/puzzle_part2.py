import os
import re

SIMULATION_TIME = 1


def map_robots(input_file_path: str):
    with open(input_file_path, "r") as file:
        robots = re.findall(r"(\d+),(\d+).*?(-?\d+),(-?\d+)", file.read())

    return robots


def simulate_robot(robot, cycles) -> tuple:
    px, py, vx, vy = map(int, robot)

    sum_x = px + vx * cycles
    sum_y = py + vy * cycles

    new_x = sum_x % map_width
    new_y = sum_y % map_height

    return (new_x, new_y, vx, vy)


def print_map(robots):
    for col in range(map_width):
        for row in range(map_height):
            if (row, col) in [(x, y) for x, y, _, _ in robots]:
                print("X", end="")
            else:
                print(".", end="")
        else:
            print()
    else:
        print()


def solve(input_file_path: str) -> int:
    robots = map_robots(input_file_path)
    num_robots = len(robots)

    time = 0
    while True:
        time += 1
        robots = list(map(lambda robot: simulate_robot(robot, SIMULATION_TIME), robots))

        if len(set([(x, y) for x, y, _, _ in robots])) == num_robots:
            print_map(robots)
            return time


if __name__ == "__main__":
    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )

    global map_width
    map_width = 101
    global map_height
    map_height = 103
    print(f"Result: {solve(input_file_path)}")
