from typing import Tuple


def part_1(input: list) -> int:
    (coordinates, folds) = parse(input)
    fold(coordinates, [folds[0]])
    return len(coordinates)


def part_2(input: list) -> list:
    (coordinates, folds) = parse(input)
    fold(coordinates, folds)
    return printed_coordinates(coordinates)


def parse(input: list) -> Tuple[set, list]:
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
    # updates coordinates based on the list of folds
    for (direction, amount) in folds:
        for coordinate in list(coordinates):
            x, y = coordinate
            if direction == "x":
                if x > amount:
                    coordinates.remove(coordinate)
                    coordinates.add((amount * 2 - x, y))
            elif direction == "y":
                if y > amount:
                    coordinates.remove(coordinate)
                    coordinates.add((x, amount * 2 - y))


def printed_coordinates(coordinates: set) -> list:
    result = []
    max_x = max(c[0] for c in coordinates)
    max_y = max(c[1] for c in coordinates)
    for y in range(max_y + 1):
        row = ""
        for x in range(max_x + 1):
            row += "#" if (x, y) in coordinates else "."
        result.append(row)

    return result
