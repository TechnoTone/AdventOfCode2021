from functools import reduce


def part_1(input: list) -> int:
    width = len(input[0])
    height = len(input)

    low_points = lowPoints(input)

    risk = 0

    for x, y in low_points:
        risk += 1 + input[y][x]

    return risk


def part_2(input: list) -> int:
    width = len(input[0])
    height = len(input)

    low_points = lowPoints(input)

    basins = []

    for x, y in low_points:
        basins.append(expandBasin(x, y, input))

    basins.sort(reverse=True)
    return reduce(lambda x, y: x * y, basins[:3])


def lowPoints(heightmap: list) -> list:
    width = len(heightmap[0])
    height = len(heightmap)

    def loc(x, y):
        if x < 0 or x >= width or y < 0 or y >= height:
            return 10
        return heightmap[y][x]

    lows = []

    for y in range(height):
        for x in range(width):
            loc_height = loc(x, y)
            if (
                loc_height < loc(x - 1, y)
                and loc_height < loc(x + 1, y)
                and loc_height < loc(x, y - 1)
                and loc_height < loc(x, y + 1)
            ):
                lows.append((x, y))

    return lows


def expandBasin(x, y, heightmap):
    width = len(heightmap[0])
    height = len(heightmap)

    locations = set()
    edges = []
    edges.append((x, y))

    def loc(x, y):
        if x >= 0 and x < width and y >= 0 and y < height:
            if heightmap[y][x] < 9:
                return heightmap[y][x]
        return -1

    while len(edges) > 0:
        x, y = edges.pop()

        if (x, y) in locations:
            continue

        locations.add((x, y))

        loc_height = loc(x, y)
        if loc(x - 1, y) > loc_height:
            edges.append((x - 1, y))
        if loc(x + 1, y) > loc_height:
            edges.append((x + 1, y))
        if loc(x, y - 1) > loc_height:
            edges.append((x, y - 1))
        if loc(x, y + 1) > loc_height:
            edges.append((x, y + 1))

    return len(locations)
