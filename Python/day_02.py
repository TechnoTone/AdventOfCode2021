import utils


def parse(input: str) -> (int, int):
    direction = input.split()[0]
    distance = int(input.split()[1])

    if direction == 'forward':
        return (distance, 0)
    elif direction == 'backward':
        return (-distance, 0)
    elif direction == 'down':
        return (0, distance)
    elif direction == 'up':
        return (0, -distance)

    return (0, 0)


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
