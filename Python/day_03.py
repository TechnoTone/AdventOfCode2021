import utils


def bitCounts(input: list, pos: int) -> int:
    return len(list(filter(lambda x: x[pos] == '1', input)))


def part_1(input: list) -> int:
    result = 0
    for n in range(len(input[0])):
        if bitCounts(input, n) * 2 >= len(input):
            result = result * 2 + 1
        else:
            result = result * 2

    max = 2 ** len(input[0]) - 1

    return result * (max - result)


def filterCandidates(fn, candidates, pos=0) -> int:
    if len(candidates) == 1:
        return int(candidates[0], 2)

    target = '1' if fn(bitCounts(candidates, pos) *
                       2, len(candidates)) else '0'

    return filterCandidates(fn, list(filter(lambda x: x[pos] == target, candidates)), pos + 1)


def part_2(input: list) -> int:
    return filterCandidates(lambda a, b: a >= b, input) * filterCandidates(lambda a, b: a < b, input)
