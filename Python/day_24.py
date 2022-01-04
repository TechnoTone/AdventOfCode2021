from typing import Tuple


def part_1(program: list) -> int:

    subroutines = []
    for instruction in program:
        if instruction.startswith("inp"):
            subroutines.append([])
        subroutines[-1].append(instruction)

    pairs = []
    stack = []
    for i, subroutine in enumerate(subroutines):
        if subroutine[4] == "div z 1":
            stack.append(i)
        else:
            pairs.append((stack.pop(), i))

    digits = [0] * 14

    for p in pairs:
        for d1 in range(9, 0, -1):
            for d2 in range(9, 0, -1):
                z1 = run_sub(subroutines[p[0]], (0, 0, 0, 0), d1)
                z2 = run_sub(subroutines[p[1]], (0, 0, 0, z1), d2)

                if z2 == 0:
                    digits[p[0]] = d1
                    digits[p[1]] = d2
                    break
            if digits[p[0]] != 0:
                break

    return int("".join(str(d) for d in digits))


def part_2(program: list) -> int:

    subroutines = []
    for instruction in program:
        if instruction.startswith("inp"):
            subroutines.append([])
        subroutines[-1].append(instruction)

    pairs = []
    stack = []
    for i, subroutine in enumerate(subroutines):
        if subroutine[4] == "div z 1":
            stack.append(i)
        else:
            pairs.append((stack.pop(), i))

    digits = [0] * 14

    for p in pairs:
        for d1 in range(1, 14):
            for d2 in range(1, 14):
                z1 = run_sub(subroutines[p[0]], (0, 0, 0, 0), d1)
                z2 = run_sub(subroutines[p[1]], (0, 0, 0, z1), d2)

                if z2 == 0:
                    digits[p[0]] = d1
                    digits[p[1]] = d2
                    break
            if digits[p[0]] != 0:
                break

    return int("".join(str(d) for d in digits))


def run_sub(subroutine: list, vars: Tuple[int, int, int, int], input: int) -> int:
    v = {"w": vars[0], "x": vars[1], "y": vars[2], "z": vars[3]}

    def get_value(var: str) -> int:
        if var in v:
            return v[var]
        return int(var)

    operation = {
        "inp": lambda a, b: input,
        "add": lambda a, b: a + b,
        "mul": lambda a, b: a * b,
        "div": lambda a, b: a // b,
        "mod": lambda a, b: a % b,
        "eql": lambda a, b: int(a == b),
    }

    for instruction in subroutine:
        op, a, b = (instruction + " 0").split(" ")[:3]
        v[a] = operation[op](v[a], get_value(b))

    return v["z"]
