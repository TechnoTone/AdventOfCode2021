import utils


def part_1(input):
    input_ints = utils.ints(input)
    last = input_ints[0]
    increases = 0

    for i in input_ints:
        if i > last:
            increases += 1
        last = i
    return increases


def part_2(input):
    input_ints = utils.ints(input)
    last = 0
    increases = 0

    for i in range(len(input_ints)-2):
        window = sum(input_ints[i:i+3])
        if i > 0 and window > last:
            increases += 1
        last = window
    return increases
