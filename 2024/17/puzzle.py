import os
import re
import time

input = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")


def parse_input(input: str) -> tuple:
    with open(input, "r") as file:
        a, b, c, program = re.findall(
            r"(\d+).*?(\d+).*?(\d+).*?(\d(?:,\d)*)", file.read(), re.S
        )[0]

    return int(a), int(b), int(c), list(map(int, program.split(",")))


def get_combo_operand(operand, register_a, register_b, register_c):

    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return register_a
        case 5:
            return register_b
        case 6:
            return register_c
        case 7:
            raise ValueError("7 is not a valid operand")


def run_program(
    register_a: int, register_b: int, register_c: int, program: list
) -> list:
    pointer = 0
    output = []

    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]

        # print(f"Pointer: {pointer}, Opcode: {opcode}, Operand: {operand}")
        combo = get_combo_operand(operand, register_a, register_b, register_c)
        match opcode:
            case 0:
                register_a = register_a >> combo
            case 1:
                register_b = register_b ^ operand
            case 2:
                register_b = combo % 8  # or &7 for bitwise AND
            case 3:
                pointer = operand - 2 if register_a != 0 else float("inf")
            case 4:
                register_b = register_b ^ register_c
            case 5:
                output.append(combo & 7)  # or %8
            case 6:
                register_b = register_a >> combo
            case 7:
                register_c = register_a >> combo
        pointer += 2

    return output


def search_a() -> int:
    _, register_b, register_c, program = parse_input(input)
    search_a = 0

    for i in range(1, len(program) + 1):
        sub = program[len(program) - i :]

        search_a = search_a << 3

        while True:
            output = run_program(search_a, register_b, register_c, program)

            if output == sub:
                break
            else:
                search_a += 1

    return search_a


if __name__ == "__main__":
    print("-" * 10 + "PART 1" + "-" * 10)
    start_time = time.time()
    a, b, c, program = parse_input(input)
    print(f"Result: {run_program(a, b, c, program)}")
    print(f"Duration: {round(time.time() - start_time, 2)} s", end="\n\n")

    print("-" * 10 + "PART 2" + "-" * 10)
    start_time = time.time()
    print(f"Result: {search_a()}")
    print(f"Duration: {round(time.time() - start_time, 2)} s", end="\n\n")
