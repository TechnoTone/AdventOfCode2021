import statistics
from collections import Counter


def part_1(input: list) -> int:
    return sum(map(lambda x: abs(x - statistics.median(input)), input))


def part_2(input: list) -> int:
    counts = Counter(input)
    _min = min(counts)
    _max = max(counts)

    total_fuel = Counter()
    for num in range(_min, _max + 1):
        for k, v in counts.items():
            total_fuel[num] += triangle(abs(num - k)) * v

    return min(total_fuel.values())


def triangle(n: int) -> int:
    return n * (n + 1) // 2
