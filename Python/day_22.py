import re
from Extras import Cuboid, Point3D


def part_1(input: list) -> int:
    return answer(input, True)


def part_2(input: list) -> int:
    return answer(input, False)


def answer(input: list, rebooting: bool) -> int:
    cuboids = set()

    for (state, next) in parse(input, rebooting):
        overlapping = list(filter(lambda c: c.intersects(next), cuboids))

        for c in overlapping:
            cuboids.remove(c)
            intersection = next.intersection(c)
            if intersection != c:
                remainders = c.cut(intersection)
                cuboids |= set(remainders)

        if state:
            cuboids.add(next)

    return sum(cuboid.volume() for cuboid in cuboids)


def parse(input: list, rebooting) -> list:
    for line in input:
        [state, rest] = line.split()
        state = state == "on"

        [x, y, z] = map(
            lambda s: re.search("[xyz]=(-?\d+)..(-?\d+)", s).groups(), rest.split(",")
        )

        min = Point3D(int(x[0]), int(y[0]), int(z[0]))
        max = Point3D(int(x[1]), int(y[1]), int(z[1]))

        if rebooting:
            init_area = Cuboid(Point3D(-50, -50, -50), Point3D(50, 50, 50))

            if (
                min.x <= init_area.max.x
                and min.y <= init_area.max.y
                and min.z <= init_area.max.z
            ) and (
                max.x >= init_area.min.x
                and max.y >= init_area.min.y
                and max.z >= init_area.min.z
            ):
                yield (state, init_area.intersection(Cuboid(min, max)))

        else:
            yield (state, Cuboid(min, max))

        pass
