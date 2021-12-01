def read_input_file(day: int):
    with open(f'input/day{day}.txt') as f:
        return f.read()


def lines(input):
    return list(input.splitlines())


def ints(input):
    return list(map(int, lines(input)))
