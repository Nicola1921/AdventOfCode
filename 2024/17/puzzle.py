import math
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


# Opcode 0
def adv(operand: int) -> None:
    global register_a

    numerator = register_a
    denominator = math.pow(2, get_combo_operand(operand))

    register_a = int(numerator / denominator)


# Opcode 1
def bxl(operand: int) -> None:
    global register_b

    register_b = register_b ^ operand


# Opcode 2
def bst(operand: int) -> None:
    global register_b

    combo_operand = get_combo_operand(operand)
    register_b = combo_operand % 8


# Opcode 3
def jnz(operand: int) -> None:
    global register_a, pointer

    if register_a == 0:
        pointer = float("inf")
        return

    pointer = operand


# Opcode 4
def bxc() -> None:
    global register_b, register_c

    register_b = register_b ^ register_c


# Opcode 5
def out(operand: int) -> None:
    global output

    combo_operand = get_combo_operand(operand)
    value = combo_operand % 8
    output.append(str(value))


# Opcode 6
def bdv(operand: int) -> None:
    global register_a, register_b

    numerator = register_a
    denominator = math.pow(2, get_combo_operand(operand))

    register_b = int(numerator / denominator)


# Opcode 7
def cdv(operand: int) -> None:
    global register_a, register_c

    numerator = register_a
    denominator = math.pow(2, get_combo_operand(operand))

    register_c = int(numerator / denominator)


def run_instruction(opcode: int, operand: int):
    global pointer

    match opcode:
        case 0:
            adv(operand)
            pointer += 2
        case 1:
            bxl(operand)
            pointer += 2
        case 2:
            bst(operand)
            pointer += 2
        case 3:
            jnz(operand)
        case 4:
            bxc()
            pointer += 2
        case 5:
            out(operand)
            pointer += 2
        case 6:
            bdv(operand)
            pointer += 2
        case 7:
            cdv(operand)
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
