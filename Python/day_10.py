from functools import reduce


def part_1(input: list) -> int:
    return sum(syntaxErrorScore(line) for line in input)


def part_2(input: list) -> int:
    scores = sorted(list(filter(greaterThanZero, map(completionScore, input))))
    return scores[len(scores) // 2]


def greaterThanZero(value: int) -> bool:
    return value > 0


matching = {}
matching["("] = ")"
matching["["] = "]"
matching["{"] = "}"
matching["<"] = ">"


def syntaxErrorScore(line: str) -> int:
    scores = {}
    scores[")"] = 3
    scores["]"] = 57
    scores["}"] = 1197
    scores[">"] = 25137

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
    scores = {}
    scores["("] = 1
    scores["["] = 2
    scores["{"] = 3
    scores["<"] = 4

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

    score = 0
    while len(chunks) > 0:
        score = score * 5 + scores[chunks.pop()]

    return score


def isOpening(char: str) -> bool:
    return char in matching
