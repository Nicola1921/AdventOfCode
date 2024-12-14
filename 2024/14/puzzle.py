import math
import os
import re
import unittest
from functools import reduce
from operator import mul

SIMULATION_TIME = 100


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

    if new_x < 0:
        new_x = map_width - new_x

    if new_y < 0:
        new_y = map_height - new_y

    return (new_x, new_y)


def solve(input_file_path: str) -> int:
    robots = map_robots(input_file_path)

    positions = list(map(lambda robot: simulate_robot(robot, 100), robots))

    split_width = map_width / 2
    split_height = map_height / 2

    quadrants = [0] * 4
    for pos in positions:
        if pos[0] < math.floor(split_width):
            if pos[1] < math.floor(split_height):
                quadrants[3] += 1
            elif pos[1] >= math.ceil(split_height):
                quadrants[2] += 1
        elif pos[0] >= math.ceil(split_width):
            if pos[1] < math.floor(split_height):
                quadrants[0] += 1
            elif pos[1] >= math.ceil(split_height):
                quadrants[1] += 1
    return reduce(mul, quadrants)


class Test(unittest.TestCase):
    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )
        global map_width
        map_width = 11
        global map_height
        map_height = 7
        self.assertEqual(solve(input_file_path), 12)


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    global map_width
    map_width = 101
    global map_height
    map_height = 103
    print(f"Result: {solve(input_file_path)}")
