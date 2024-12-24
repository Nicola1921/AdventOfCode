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


def calculate_logic_gate(inp_vals: dict, logic_gates: dict, key: str) -> int:
    inp_val = inp_vals.get(key)

    if inp_val is not None:
        return inp_val

    lg = logic_gates.get(key).split()
    match (lg[1]):
        case "AND":
            return calculate_logic_gate(
                inp_vals, logic_gates, lg[0]
            ) & calculate_logic_gate(inp_vals, logic_gates, lg[2])
        case "OR":
            return calculate_logic_gate(
                inp_vals, logic_gates, lg[0]
            ) | calculate_logic_gate(inp_vals, logic_gates, lg[2])
        case "XOR":
            return calculate_logic_gate(
                inp_vals, logic_gates, lg[0]
            ) ^ calculate_logic_gate(inp_vals, logic_gates, lg[2])


def solve() -> int:
    inp_vals, logic_gates = parse_file()

    z_keys = sorted(
        [key for key in logic_gates.keys() if key.startswith("z")], reverse=True
    )

    z_values = [calculate_logic_gate(inp_vals, logic_gates, key) for key in z_keys]

    return int("".join(map(str, z_values)), base=2)


if __name__ == "__main__":

    print("-" * 10 + "PART 1" + "-" * 10)
    start_time = time.time()
    print(f"Result: {solve()}")
    print(f"Duration: {round(time.time() - start_time, 2)} s", end="\n\n")
