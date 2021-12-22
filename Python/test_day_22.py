from Extras import Cuboid, Point3D
import day_22
from utils import Input

EXAMPLE1 = Input.ex(22, 1).lines()
EXAMPLE2 = Input.ex(22, 2).lines()
DATA = Input.day(22).lines()


def test_day_22_cuboid_cut():
    a = Cuboid(Point3D(0, 0, 0), Point3D(2, 2, 2))
    b = Cuboid(Point3D(1, 1, 1), Point3D(1, 1, 1))

    assert a.cut(a) == []
    assert b.cut(b) == []
    assert b.cut(a) == []

    remainders = a.cut(b)
    assert len(remainders) == 6

    cubes = list(q for c in remainders for q in list(c.cubes()))
    assert Point3D(1, 1, 1) not in cubes
    assert len(cubes) == 26
    assert len(set(cubes)) == 26


def test_day_22_part_1_ex_01():
    assert day_22.part_1(EXAMPLE1) == 590784


def test_day_22_part_1_solution():
    assert day_22.part_1(DATA) == 600458


def test_day_22_part_2_ex_02():
    assert day_22.part_2(EXAMPLE2) == 2758514936282235


def test_day_22_part_2_solution():
    assert day_22.part_2(DATA) == 1334275219162622
