import os
import unittest


def find_free_space(free_spaces: list, size: int) -> int:

    for i in range(len(free_spaces)):
        free_space_info = free_spaces[i]
        if free_space_info[1] >= size:
            return free_space_info[0]

    return -1


def allocate_space(
    free_spaces: list, allocate_idx: int, free_idx: int, size: int
) -> None:

    for i in range(len(free_spaces)):
        free_space_info = free_spaces[i]

        if free_space_info[0] != allocate_idx:
            continue

        free_spaces.pop(i)
        if size < free_space_info[1]:
            free_spaces.insert(i, (allocate_idx + size, free_space_info[1] - size))

        return


def solve(input_file_path: str) -> int:
    checksum = 0
    with open(input_file_path, "r") as file:
        disk = list(map(int, file.readline()))

        files = dict()
        free_spaces = []
        for idx, num in enumerate(disk):
            if idx % 2 == 0:
                files[int(idx / 2)] = (sum(disk[:idx]), num)
            else:
                free_spaces.append((sum(disk[:idx]), num))

        for file_id in range(max(files.keys()), -1, -1):
            file_info = files.get(file_id)
            start_idx = file_info[0]
            size = file_info[1]

            free_space_idx = find_free_space(free_spaces, size)
            if free_space_idx != -1 and free_space_idx < start_idx:
                files.update({file_id: (free_space_idx, size)})
                allocate_space(free_spaces, free_space_idx, start_idx, size)

        checksum = 0
        for key, value in files.items():
            for i in range(value[0], value[0] + value[1]):
                checksum += i * key

    return checksum


class Test(unittest.TestCase):

    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(solve(input_file_path), 2858)


import time

if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    start_Time = time.time()
    print(f"Result: {solve(input_file_path)}")
    print(f"Duration: {round(time.time() - start_Time, 4)} s")
