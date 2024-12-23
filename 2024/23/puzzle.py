import os
import time
from collections import defaultdict
from itertools import combinations

input_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")


def parse_file() -> dict:
    com_con = defaultdict(set)

    with open(input_file_path, "r") as file:
        connections = [line.split("-") for line in file.read().splitlines()]

    for con in connections:
        com_con[con[0]].add(con[1])
        com_con[con[1]].add(con[0])

    return com_con


def solve() -> int:
    com_con = parse_file()
    lan = set()

    for com in com_con:
        if not com.startswith("t"):
            continue

        for con in com_con.get(com):
            intersec = set(com_con.get(com)).intersection(set(com_con.get(con)))

            for ints in intersec:
                l = [com, con, ints]
                l.sort()
                lan.add("-".join(l))

    return len(lan)


def solve2() -> int:
    com_con = parse_file()
    lan = set()

    for com in com_con:
        for con in com_con.get(com):
            intersec = (
                set(com_con.get(com))
                .intersection(set(com_con.get(con)))
                .union({com, con})
            )

            best_intersec = set()
            for i in range(len(intersec), 2, -1):
                if i <= len(best_intersec):
                    break
                for combi in combinations(intersec, i):
                    all_con = list(
                        map(
                            set,
                            (
                                com_con.get(combi_elem).union({combi_elem})
                                for combi_elem in combi
                            ),
                        )
                    )
                    all_con_intersec = set.intersection(*all_con)
                    if len(all_con_intersec) > len(best_intersec):
                        best_intersec = all_con_intersec

            lan.add(",".join(sorted(best_intersec)))

    return max(lan, key=len)


if __name__ == "__main__":
    print("-" * 10 + "PART 1" + "-" * 10)
    start_time = time.time()
    print(f"Result: {solve()}")
    print(f"Duration: {round(time.time() - start_time, 2)} s", end="\n\n")
    print("-" * 10 + "PART 2" + "-" * 10)
    start_time = time.time()
    print(f"Result: {solve2()}")
    print(f"Duration: {round(time.time() - start_time, 2)} s", end="\n\n")
