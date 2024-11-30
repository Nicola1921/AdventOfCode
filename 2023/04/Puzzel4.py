import os
import re
import unittest


def solve(input_file_path: str) -> tuple:
    with open(input_file_path, "r") as file:
        scratch_card_worth = 0
        for line in file:
            (winning_numbers, your_numbers) = line.split(":")[1].split("|")
            set_winning_numbers = set(winning_numbers.split())
            set_your_numbers = set(your_numbers.split())

            your_win_numbers = set_your_numbers & set_winning_numbers
            if len(your_win_numbers) > 0:
                scratch_card_worth += 2 ** (len(your_win_numbers) - 1)

        return scratch_card_worth, 0


class Test(unittest.TestCase):
    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(solve(input_file_path), (13, 0))


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    print(f"Result: {solve(input_file_path)}")
