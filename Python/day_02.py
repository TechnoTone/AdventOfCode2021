from typing import Tuple


def part_1(input: list) -> int:
    values = [parse(line) for line in input]
    horizontal = 0
    depth = 0
    for i, j in values:
        horizontal += i
        depth += j

    return horizontal * depth


def part_2(input: list) -> int:
    values = [parse(line) for line in input]
    horizontal = 0
    depth = 0
    aim = 0
    for i, j in values:
        horizontal += i
        depth += aim * i
        aim += j

    return horizontal * depth


def parse(input: str) -> Tuple[int, int]:
    match input.split():
        case 'forward', distance:
            return (int(distance), 0)
        case "down", distance:
            return (0, int(distance))
        case 'up', distance:
            return (0, -int(distance))

    return (0, 0)
