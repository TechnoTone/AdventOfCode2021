import utils


def bitCounts(input: list, pos: int) -> int:
    return len(list(filter(lambda x: x[pos] == '1', input)))


def part_1(input: list) -> int:
    gamma = ''
    epsilon = ''
    for n in range(len(input[0])):
        if bitCounts(input, n) * 2 > len(input):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, 2) * int(epsilon, 2)


def filterCandidates(fn, candidates) -> int:
    n = 0
    while len(candidates) > 1:
        if fn(bitCounts(candidates, n)*2, len(candidates)):
            candidates = list(filter(lambda x: x[n] == '1', candidates))
        else:
            candidates = list(filter(lambda x: x[n] == '0', candidates))
        n += 1

    return int(candidates[0], 2)


def part_2(input: list) -> int:
    ogr = filterCandidates(lambda a, b: a >= b, input)
    csr = filterCandidates(lambda a, b: a < b, input)

    return ogr * csr
