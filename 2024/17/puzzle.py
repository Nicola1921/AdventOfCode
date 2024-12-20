import os
import re
import time

input = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")
with open(input, "r") as file:
    a, b, c, program = re.findall(
        r"(\d+).*?(\d+).*?(\d+).*?(\d(?:,\d)*)", file.read(), re.S
    )[0]

register_a = int(a)
register_b = int(b)
register_c = int(c)
program = list(map(int, program.split(",")))
pointer = 0
output = []


def get_combo_operand(operand):
    global register_a, register_b, register_c

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


def run_instruction(opcode: int, operand: int):
    global register_a, register_b, register_c, pointer

    match opcode:
        case 0:
            register_a = register_a >> get_combo_operand(operand)
        case 1:
            register_b = register_b ^ operand
        case 2:
            register_b = get_combo_operand(operand) % 8  # or &7 for bitwise AND
        case 3:
            pointer = operand - 2 if register_a != 0 else float("inf")
        case 4:
            register_b = register_b ^ register_c
        case 5:
            output.append(str(get_combo_operand(operand) & 7))  # or %8
        case 6:
            register_b = register_a >> get_combo_operand(operand)
        case 7:
            register_c = register_a >> get_combo_operand(operand)

    pointer += 2


def solve() -> int:
    global pointer, program, output

    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]

        print(f"Pointer: {pointer}, Opcode: {opcode}, Operand: {operand}")
        run_instruction(opcode, operand)

    return ",".join(output)


if __name__ == "__main__":
    print("-" * 10 + "PART 1" + "-" * 10)
    start_time = time.time()
    print(f"Result: {solve()}")
    print(f"Duration: {round(time.time() - start_time, 2)} s", end="\n\n")
