def part_1(input: list) -> int:
    total_flashes = 0
    for _ in range(100):
        flashes, input = step(input)
        total_flashes += flashes

    return total_flashes


def part_2(input: list) -> int:
    steps = 0
    while True:
        steps += 1
        flashes, input = step(input)
        if flashes == 100:  # All octopuses flashed
            return steps


def step(input: list) -> list:
    width = len(input[0])
    height = len(input)

    def get_value(x, y):
        if x < 0 or x >= width or y < 0 or y >= height:
            return 0
        return input[y][x]

    result = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(get_value(x, y) + 1)
        result.append(row)

    def flash(x, y):
        x_min = max(0, x - 1)
        x_max = min(width - 1, x + 1)
        y_min = max(0, y - 1)
        y_max = min(height - 1, y + 1)
        for y in range(y_min, y_max + 1):
            for x in range(x_min, x_max + 1):
                if result[y][x] < 10:
                    result[y][x] += 1

    flashCheck = True
    flashes = 0
    while flashCheck:
        flashCheck = False
        for y in range(height):
            for x in range(width):
                if result[y][x] == 10:
                    flashCheck = True
                    flashes += 1
                    flash(x, y)
                    result[y][x] = 11

    for y in range(height):
        for x in range(width):
            if result[y][x] == 11:
                result[y][x] = 0

    return flashes, result
