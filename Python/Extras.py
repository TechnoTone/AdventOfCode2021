from math import remainder


class Point3D:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __sub__(self, other):
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __lt__(self, other):
        return (self.x, self.y, self.z) < (other.x, other.y, other.z)

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def rotate_x(self):
        return Point3D(self.x, -self.z, self.y)

    def rotate_y(self):
        return Point3D(self.z, self.y, -self.x)

    def rotate_z(self):
        return Point3D(self.y, -self.x, self.z)


class Cuboid:
    def __init__(self, min: Point3D, max: Point3D):
        self.min, self.max = min, max

    def intersection(self, other):
        return Cuboid(
            Point3D(
                max(self.min.x, other.min.x),
                max(self.min.y, other.min.y),
                max(self.min.z, other.min.z),
            ),
            Point3D(
                min(self.max.x, other.max.x),
                min(self.max.y, other.max.y),
                min(self.max.z, other.max.z),
            ),
        )

    def intersects(self, other):
        return (
            self.min.x <= other.max.x
            and self.min.y <= other.max.y
            and self.min.z <= other.max.z
            and self.max.x >= other.min.x
            and self.max.y >= other.min.y
            and self.max.z >= other.min.z
        )

    def cubes(self):
        for x in range(self.min.x, self.max.x + 1):
            for y in range(self.min.y, self.max.y + 1):
                for z in range(self.min.z, self.max.z + 1):
                    yield Point3D(x, y, z)

    def volume(self):
        return (
            (abs(self.max.x - self.min.x) + 1)
            * (abs(self.max.y - self.min.y) + 1)
            * (abs(self.max.z - self.min.z) + 1)
        )

    def cut(self, other):
        s = Cuboid(self.min, self.max)
        i = self.intersection(other)

        remainders = []

        if s.min.x < i.min.x:
            remainders.append(Cuboid(s.min, Point3D(i.min.x - 1, s.max.y, s.max.z)))
            s = Cuboid(Point3D(i.min.x, s.min.y, s.min.z), s.max)
        if s.max.x > i.max.x:
            remainders.append(Cuboid(Point3D(i.max.x + 1, s.min.y, s.min.z), s.max))
            s = Cuboid(s.min, Point3D(i.max.x, s.max.y, s.max.z))

        if s.min.y < i.min.y:
            remainders.append(Cuboid(s.min, Point3D(s.max.x, i.min.y - 1, s.max.z)))
            s = Cuboid(Point3D(s.min.x, i.min.y, s.min.z), s.max)
        if s.max.y > i.max.y:
            remainders.append(Cuboid(Point3D(s.min.x, i.max.y + 1, s.min.z), s.max))
            s = Cuboid(s.min, Point3D(s.max.x, i.max.y, s.max.z))

        if s.min.z < i.min.z:
            remainders.append(Cuboid(s.min, Point3D(s.max.x, s.max.y, i.min.z - 1)))
            s = Cuboid(Point3D(s.min.x, s.min.y, i.min.z), s.max)
        if s.max.z > i.max.z:
            remainders.append(Cuboid(Point3D(s.min.x, s.min.y, i.max.z + 1), s.max))
            s = Cuboid(s.min, Point3D(s.max.x, s.max.y, i.max.z))

        return remainders

    def __eq__(self, other):
        return self.min == other.min and self.max == other.max

    def __sub__(self, other):

        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __str__(self):
        return f"{self.min}..{self.max}"

    def __repr__(self):
        return f"{self.min}..{self.max}"

    def __hash__(self):
        return hash((self.min, self.max))
