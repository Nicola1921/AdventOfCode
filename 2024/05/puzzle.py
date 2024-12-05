import math
import os
import unittest
from functools import cmp_to_key


def solve(input_file_path: str) -> int:
    rules = {}
    updates = []
    read_rules = True
    with open(input_file_path, "r") as file:
        for line in file:
            line = line.rstrip()
            if line == "":
                read_rules = False
                continue

            if read_rules:
                rule = line.split("|")
                if rule[0] in rules:
                    current_rule_data = list(rules.get(rule[0]))
                    current_rule_data.append(rule[1])
                    rules.update({rule[0]: current_rule_data})
                else:
                    rules[rule[0]] = [rule[1]]
            else:
                updates.append(line.split(","))

    sum = 0
    invalid_sum = 0
    for update in updates:
        for idx, num in enumerate(update):
            numbers_not_allowed_before = rules.get(num, [])
            for nnab in numbers_not_allowed_before:
                if nnab in update[:idx]:
                    break
            else:
                continue
            break
        else:
            sum += get_middle_num(update)
            continue

        update = sorted(update, key=cmp_to_key(lambda x, y: compare(x, y, rules)))
        invalid_sum += get_middle_num(update)

    return sum, invalid_sum


def get_middle_num(update: list) -> int:
    m_idx = math.ceil(len(update) / 2)
    return int(update[m_idx - 1])


def compare(x: str, y: str, rules: dict) -> int:
    if y in list(rules.get(x, [])):
        return -1

    return 1


def list_find(search, array):
    for i, val in enumerate(array):
        if val == search:
            return i

    return -1


class Test(unittest.TestCase):
    def test_solve(self):
        input_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "testData.txt"
        )

        self.assertEqual(solve(input_file_path), (143, 123))


if __name__ == "__main__":
    unittest.main(exit=False)

    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data.txt"
    )
    print(f"Result: {solve(input_file_path)}")
