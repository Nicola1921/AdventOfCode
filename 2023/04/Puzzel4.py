import os
import unittest


def solve(input_file_path: str) -> int:
    with open(input_file_path, "r") as file:
        lines = file.readlines()
        scratch_card_worth = 0
        copies = [1] * len(lines)
        for idx, line in enumerate(lines):
            (winning_numbers, your_numbers) = line.split(":")[1].split("|")
            set_winning_numbers = set(winning_numbers.split())
            set_your_numbers = set(your_numbers.split())

            your_win_numbers = set_your_numbers & set_winning_numbers
            count_of_your_win_numbers = len(your_win_numbers)

            if count_of_your_win_numbers > 0:
                scratch_card_worth += 2 ** (count_of_your_win_numbers - 1)

            for i in range(1, 1 + count_of_your_win_numbers):
                copies[idx + i] += copies[idx]

        return scratch_card_worth, sum(copies)


class Test(unittest.TestCase):
    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(solve(input_file_path), (13, 30))


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    print(f"Result: {solve(input_file_path)}")
