def part_1(input: list) -> int:
    vents = parse(input)
    return len([1 for v in vents.values() if v > 1])


def part_2(input: list) -> int:
    vents = parse(input, True)
    return len([1 for v in vents.values() if v > 1])


def parse(input: list, includeDiagonals=False) -> dict:
    result = {}
    for line in input:
        [(x1, y1), (x2, y2)] = map(parseCoord, line.split(' -> '))
        if (x1 == x2):
            for y in range((min(y1, y2)), (max(y1, y2))+1):
                result[(x1, y)] = result.get((x1, y), 0) + 1
        elif (y1 == y2):
            for x in range((min(x1, x2)), (max(x1, x2))+1):
                result[(x, y1)] = result.get((x, y1), 0) + 1

        elif includeDiagonals:
            length = abs(x1 - x2)
            dx = (x2 - x1) / length
            dy = (y2 - y1) / length
            for n in range(length + 1):
                x = x1 + (dx * n)
                y = y1 + (dy * n)
                result[(x, y)] = result.get((x, y), 0) + 1

    return result


def parseCoord(coord: str) -> tuple:
    x, y = coord.split(',')
    return int(x), int(y)
