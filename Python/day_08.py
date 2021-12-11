from functools import cmp_to_key


def part_1(input: list) -> int:
    signals = map(parseLine, input)
    counts = map(countDigits, signals)
    return sum(counts)


def part_2(input: list) -> int:
    signals = map(parseLine, input)
    values = map(value, signals)
    return sum(values)


def parseLine(input: str) -> list:
    return list(map(lambda s: s.split(), input.split(" | ")))


def countDigits(signal: list) -> int:
    return len(knownDigits(signal))


def knownDigits(signal: list) -> list:
    return list(filter(lambda d: len(d) in (2, 3, 4, 7), signal[1]))


SEGMENT_COUNTS = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


def value(signal: list) -> int:
    patterns = sortedItems(signal[0])
    digits = sortedItems(signal[1])

    byLength = {2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    d = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}

    for pattern in patterns:
        l = len(pattern)
        if l in byLength:
            byLength[l].append(pattern)
        else:
            byLength[l] = [pattern]

    d[1] = byLength[2][0]
    d[4] = byLength[4][0]
    d[7] = byLength[3][0]
    d[8] = byLength[7][0]

    d[3] = firstContaining(byLength[5], d[1])
    d[6] = firstNotContaining(byLength[6], d[1])
    d[9] = firstContaining(byLength[6], d[4])
    d[0] = remaining(byLength[6], [d[6], d[9]])

    _2or5 = excluding(byLength[5], [d[3]])
    if containsAll(d[6], _2or5[0]):
        d[5] = _2or5[0]
        d[2] = _2or5[1]
    else:
        d[5] = _2or5[1]
        d[2] = _2or5[0]

    matches = {}
    for key in d:
        matches[d[key]] = str(key)

    return int("".join(map(matches.get, digits)))


def sortedItems(items: list) -> list:
    return list(map(lambda s: "".join(sorted(s)), items))


def firstContaining(items: list, pattern: str) -> str:
    for item in items:
        if containsAll(item, pattern):
            return item


def containsAll(a: list, b: list) -> bool:
    return len(intersect(a, b)) == len(b)


def firstNotContaining(items: list, pattern: str) -> str:
    for item in items:
        if not containsAll(item, pattern):
            return item


def remaining(items: list, exclude: list) -> str:
    return excluding(items, exclude)[0]


def excluding(items: list, exclude: list) -> list:
    return list(filter(lambda i: i not in exclude, items))


def intersect(a: list, b: list) -> list:
    return list(filter(lambda i: i in b, a))


# Some notes I used to examine the relationships between
# the 7 segments of the digits and to find any patterns:
#
#
#    0:      1:      2:      3:      4:      5:      6:      7:      8:      9:
#   aaaa    ....    aaaa    aaaa    ....    aaaa    aaaa    aaaa    aaaa    aaaa
#  b    c  .    c  .    c  .    c  b    c  b    .  b    .  .    c  b    c  b    c
#  b    c  .    c  .    c  .    c  b    c  b    .  b    .  .    c  b    c  b    c
#   ....    ....    dddd    dddd    dddd    dddd    dddd    ....    dddd    dddd
#  e    f  .    f  e    .  .    f  .    f  .    f  e    f  .    f  e    f  .    f
#  e    f  .    f  e    .  .    f  .    f  .    f  e    f  .    f  e    f  .    f
#   gggg    ....    gggg    gggg    ....    gggg    gggg    ....    gggg    gggg
#
#
#   0   a b c   e f g       6
#   1       c     f     2
#   2   a   c d e   g      5
#   3   a   c d   f g      5
#   4     b c d   f       4
#   5   a b   d   f g      5
#   6   a b   d e f g       6
#   7   a   c     f      3
#   8   a b c d e f g        7
#   9   a b c d   f g       6
