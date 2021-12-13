def part_1(input: list) -> int:
    (coordinates, folds) = parse(input)
    fold(coordinates, [folds[0]])
    return len(coordinates)


def part_2(input: list) -> int:
    (coordinates, folds) = parse(input)
    fold(coordinates, folds)
    return printed_coordinates(coordinates)


def parse(input: list) -> (set, list):
    coordinates = set()
    folds = []

    for line in input:
        if "," in line:
            coordinates.add(tuple(map(int, line.split(","))))
        elif "=" in line:
            direction = line.split("=")[0][-1]
            amount = int(line.split("=")[1])
            folds.append((direction, amount))

    return (coordinates, folds)


def fold(coordinates: set, folds: list):
    for (direction, amount) in folds:
        for coordinate in list(coordinates):
            if direction == "x":
                if coordinate[0] > amount:
                    coordinates.remove(coordinate)
                    coordinates.add((amount * 2 - coordinate[0], coordinate[1]))
            elif direction == "y":
                if coordinate[1] > amount:
                    coordinates.remove(coordinate)
                    coordinates.add((coordinate[0], amount * 2 - coordinate[1]))


def printed_coordinates(coordinates):
    result = []
    max_x = max(map(lambda c: c[0], coordinates))
    max_y = max(map(lambda c: c[1], coordinates))
    for y in range(max_y + 1):
        row = ""
        for x in range(max_x + 1):
            row += "#" if (x, y) in coordinates else "."
        result.append(row)

    return result
