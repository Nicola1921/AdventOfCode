import os
import unittest


def solve(input_file_path: str) -> int:
    with open(input_file_path, "r") as file:
        disk = list(map(int, file.readline()))

        disk_blocks = []

        for idx, num in enumerate(disk):
            if idx % 2 == 0:
                disk_blocks += [int(idx / 2)] * num
            else:
                disk_blocks += [-1] * num

        checksum = 0
        tail_idx = len(disk_blocks) - 1
        for head_idx, block in enumerate(disk_blocks):
            if head_idx > tail_idx:
                break

            if block != -1:
                checksum += head_idx * block
                continue

            checksum += head_idx * disk_blocks[tail_idx]

            while True:
                tail_idx -= 1

                if disk_blocks[tail_idx] != -1:
                    break

    return checksum


class Test(unittest.TestCase):

    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(solve(input_file_path), 1928)


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    print(f"Result: {solve(input_file_path)}")
