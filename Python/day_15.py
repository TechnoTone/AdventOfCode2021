import sys


def part_1(input: list) -> int:
    return lowestRiskPath(input)


def part_2(input: list) -> int:
    tiles = tile(input)
    return lowestRiskPath(tiles)


def lowestRiskPath(input: list) -> int:
    paths = {}
    for y in range(len(input)):
        for x in range(len(input[0])):
            paths[(x, y)] = sys.maxsize

    paths[(0, 0)] = 0

    end_loc = (len(input[0]) - 1, len(input) - 1)
    end = sys.maxsize

    def is_valid(loc: tuple) -> bool:
        return 0 <= loc[0] < len(input[0]) and 0 <= loc[1] < len(input)

    def neighbours(x: int, y: int) -> list:
        return list(filter(is_valid, [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]))

    def path(loc: tuple) -> int:
        return paths[loc]

    def risk(loc: tuple) -> int:
        return input[loc[1]][loc[0]]

    # Dijkstra to the rescue!
    # Except it isn't really Dijkstra, just inspired by him.
    while True:
        for y in range(len(input[0])):
            for x in range(len(input)):
                foo = neighbours(x, y)
                bar = map(path, foo)
                smallest = min(bar)
                if path((x, y)) > smallest + risk((x, y)):
                    paths[(x, y)] = smallest + risk((x, y))

        if paths[end_loc] < end:
            end = paths[end_loc]
        else:
            return end


def tile(input: list) -> list:
    tiles = []

    for ty in range(5):
        for y in range(len(input)):
            row = []
            for tx in range(5):
                for x in range(len(input[0])):
                    r = input[y][x] + tx + ty
                    if r > 9:
                        r -= 9
                    row.append(r)
            tiles.append(row)

    return tiles
