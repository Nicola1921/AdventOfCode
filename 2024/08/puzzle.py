import os
import unittest
from itertools import combinations

EMPTY_CHAR = "."

max_size = ()


def is_within_bounds(pos: tuple) -> bool:
    if pos[0] >= max_size[0] or pos[0] < 0:
        return False
    if pos[1] >= max_size[1] or pos[1] < 0:
        return False

    return True


def locate_antennas(input_file_path: str) -> dict:
    antennas = dict()
    with open(input_file_path, "r") as file:
        lines = file.readlines()
        global max_size
        max_size = (len(lines), len(lines[0].rstrip()))
        for row, line in enumerate(lines):
            for col, char in enumerate(line.rstrip()):

                if char == EMPTY_CHAR:
                    continue

                if char in antennas:
                    positions = list(antennas.get(char))
                    positions.append((row, col))
                    antennas.update({char: positions})
                else:
                    antennas[char] = [(row, col)]

    return antennas


def solve(input_file_path: str) -> int:
    antinodes = set()
    antennas = locate_antennas(input_file_path)
    for antenna in antennas:
        locations = antennas.get(antenna)

        com = combinations(locations, 2)

        for c in com:
            p0 = c[0]
            p1 = c[1]
            delta = (p1[0] - p0[0], p1[1] - p0[1])

            antinodeA = (p1[0] + delta[0], p1[1] + delta[1])
            antinodeB = (p0[0] - delta[0], p0[1] - delta[1])

            if is_within_bounds(antinodeA):
                antinodes.add(antinodeA)
            if is_within_bounds(antinodeB):
                antinodes.add(antinodeB)

    return len(antinodes)


class Test(unittest.TestCase):
    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(solve(input_file_path), 14)


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    print(f"Result: {solve(input_file_path)}")
