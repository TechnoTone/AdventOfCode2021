import statistics


def part_1(input: list) -> int:
    median = statistics.median(input)
    return sum(map(lambda x: abs(x - median), input))


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

    triangles = [0, 1]
    while len(triangles) <= (_max - _min):
        triangles.append(triangles[-1] + len(triangles))

    for num in range(_min, _max + 1):
        for k in unique.keys():
            total_fuel[num] += triangles[abs(num - k)] * unique[k]

    return min(total_fuel.values())
