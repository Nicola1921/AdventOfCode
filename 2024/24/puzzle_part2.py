import os
import time

input_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")


def parse_file() -> tuple[dict, dict]:
    with open(input_file_path, "r") as file:
        lines = file.read().split("\n\n")
        input_values = dict(
            [
                (inp.split(":")[0], int(inp.split(":")[1]))
                for inp in lines[0].split("\n")
            ]
        )
        logic_gates = dict(
            [
                ((lg.split("->")[1]).strip(), (lg.split("->")[0]).strip())
                for lg in lines[1].split("\n")
            ]
        )

    return input_values, logic_gates


# Full - Adder
# (A XOR B) XOR C_IN = SUM (SUM is 1 if ALL INPUTS 1 or one INPUT is 1)
# ((A XOR B) AND C_IN) OR (A AND B) = C_OUT (C_Out is 1 if >= 2 INPUTS 1)
#
# (x3 XOR y3) XOR C_x2 = z3
# ((x3 XOR y3) AND C_x2) OR (x3 AND x3) = C_x3


def solve() -> int:
    _, logic_gates = parse_file()

    wrong = set()

    lg = [logic_gates.get(key).split() + [key] for key in logic_gates]
    for op1, op, op2, key in lg:

        # Z is calculated by XOR (Except last one which is the Carry-Bit)
        if key.startswith("z") and op != "XOR" and not key == "z45":
            wrong.add(key)

        # XOR-Operation needs always an X,Y or Z Component
        if op == "XOR" and not any(
            [
                key.startswith(("x", "y", "z")),
                op1.startswith(("x", "x", "z")),
                op2.startswith(("x", "x", "z")),
            ]
        ):
            wrong.add(key)

        # Result of XOR-Operation used in an OR-Operation => WRONG
        if op == "XOR":
            if any(
                s_op == "OR" and (key == s_op1 or key == s_op2)
                for s_op1, s_op, s_op2, _ in lg
            ):
                wrong.add(key)

        # Result of AND-Operation not used in OR-Operation (Except its the first one without Carry-Bit) => WRONG
        if op == "AND" and "x00" not in [op1, op2]:
            if any(
                s_op != "OR" and (key == s_op1 or key == s_op2)
                for s_op1, s_op, s_op2, _ in lg
            ):
                wrong.add(key)

    return ",".join(sorted(wrong))


if __name__ == "__main__":

    print("-" * 10 + "PART 2" + "-" * 10)
    start_time = time.time()
    print(f"Result: {solve()}")
    print(f"Duration: {round(time.time() - start_time, 2)} s", end="\n\n")
