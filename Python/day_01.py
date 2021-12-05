def part_1(input: list) -> int:
    return increases(input, 1)


def part_2(input: list) -> int:
    return increases(input, 3)


def increases(input: list, offset: int) -> int:
    increases = 0

    for i in range(len(input) - offset):
        if input[i] < input[i + offset]:
            increases += 1

    return increases
