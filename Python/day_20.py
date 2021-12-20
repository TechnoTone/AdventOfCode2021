def part_1(input: list) -> int:
    algorithm = input[0]
    edge_toggle = algorithm[0] == "#"

    pixels = parse_pixels(input[2:])

    pixels = enhance(pixels, algorithm)
    pixels = enhance(pixels, algorithm, edge_toggle)
    return len(pixels)


def part_2(input: list) -> int:
    algorithm = input[0]
    edge_toggle = algorithm[0] == "#"

    pixels = parse_pixels(input[2:])

    for _ in range(25):  # half of 50 because it does 2 enhancements per loop
        pixels = enhance(pixels, algorithm)
        pixels = enhance(pixels, algorithm, edge_toggle)

    return len(pixels)


def render(pixels: set):
    min_x, min_y = list(map(min, zip(*pixels)))
    max_x, max_y = list(map(max, zip(*pixels)))

    output = []
    for y in range(min_y, max_y + 1):
        row = ""
        for x in range(min_x, max_x + 1):
            row += "#" if (x, y) in pixels else "."
        output.append(row)
    return output


def parse_pixels(input: list) -> set:
    return set(
        (x, y)
        for x in range(len(input[0]))
        for y in range(len(input))
        if input[y][x] == "#"
    )


def offset(p: tuple, dx: int, dy: int) -> tuple:
    return tuple(map(sum, zip(p, (dx, dy))))


def neighbours(x, y):
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            yield (x + dx, y + dy)


def enhance(pixels: set, algorithm: str, edge_is_on: bool = False) -> set:
    min_x, min_y = list(map(min, zip(*pixels)))
    max_x, max_y = list(map(max, zip(*pixels)))

    def read_value(x: int, y: int) -> str:
        def read_pixel(px: int, py: int) -> str:
            if min_x <= px <= max_x and min_y <= py <= max_y:
                return "1" if (px, py) in pixels else "0"
            return "1" if edge_is_on else "0"

        digits = [read_pixel(px, py) for (px, py) in neighbours(x, y)]
        return int("".join(digits), 2)

    output = set()
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            if algorithm[read_value(x, y)] == "#":
                output.add((x, y))

    return output
