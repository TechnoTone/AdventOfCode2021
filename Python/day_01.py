import utils


def part_1(input: list) -> int:
    last = input[0]
    increases = 0

    for i in input:
        if i > last:
            increases += 1
        last = i
    return increases


def part_2(input: list) -> int:
    last = 0
    increases = 0

    for i in range(len(input)-2):
        window = sum(input[i:i+3])
        if i > 0 and window > last:
            increases += 1
        last = window
    return increases
