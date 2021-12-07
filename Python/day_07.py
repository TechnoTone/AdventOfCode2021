import statistics


def part_1(input: list) -> int:
    return sum(map(lambda x: abs(x - statistics.median(input)), input))


def part_2(input: list) -> int:
    unique = {}
    for num in input:
        if num in unique:
            unique[num] += 1
        else:
            unique[num] = 1

    _min = min(unique.keys())
    _max = max(unique.keys())

    total_fuel = {}
    for num in range(_min, _max + 1):
        total_fuel[num] = 0

    for num in range(_min, _max + 1):
        for k in unique.keys():
            total_fuel[num] += triangle(abs(num - k)) * unique[k]

    return min(total_fuel.values())


def triangle(n: int) -> int:
    return n * (n + 1) // 2
