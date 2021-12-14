from functools import reduce


def part_1(input: list) -> int:
    return sum(syntaxErrorScore(line) for line in input)


def part_2(input: list) -> int:
    scores = sorted(list(filter(greaterThanZero, map(completionScore, input))))
    return scores[len(scores) // 2]


def greaterThanZero(value: int) -> bool:
    return value > 0


matching = {"(": ")", "[": "]", "{": "}", "<": ">"}


def syntaxErrorScore(line: str) -> int:
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}

    chunks = []
    for next in line:
        if isOpening(next):
            chunks.append(next)
        else:
            if len(chunks) == 0:  # too many closing brackets
                return 0
            opener = chunks.pop()
            if matching[opener] != next:
                return scores[next]
    # if we get here it's not a corrupt line
    return 0


def completionScore(line: str) -> int:
    scores = {"(": 1, "[": 2, "{": 3, "<": 4}

    chunks = []
    for next in line:
        if isOpening(next):
            chunks.append(next)
        else:
            if len(chunks) == 0:  # too many closing brackets
                return 0
            opener = chunks.pop()
            if matching[opener] != next:
                return 0  # corrupted line

    return reduce(lambda x, a: x * 5 + scores[a], reversed(chunks), 0)


def isOpening(char: str) -> bool:
    return char in matching
