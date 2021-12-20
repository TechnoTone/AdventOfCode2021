from collections import defaultdict
import day_19
from day_19 import Scanner, Point3D
from utils import Input

EXAMPLE1 = Input.ex(19, 1).lines()
DATA = Input.day(19).lines()


def test_day_19_rotations():
    point = Point3D(1, 2, 3)
    assert point.rotate_x() == Point3D(1, -3, 2)
    assert point.rotate_y() == Point3D(3, 2, -1)
    assert point.rotate_z() == Point3D(2, -1, 3)

    scanner = Scanner(0, [Point3D(1, 2, 3)])
    rotations = list(day_19.rotations(scanner))
    assert len(rotations) == 24

    # all 24 rotations should be unique
    beacons = [s.beacons[0] for s in rotations]
    counts = defaultdict(int)
    for b in beacons:
        counts[b] += 1

    assert len(counts) == 24
    assert all(count == 1 for count in counts.values())


def test_day_19_part_1_ex_01():
    assert day_19.part_1(EXAMPLE1) == 79


def test_day_19_part_1_solution():
    assert day_19.part_1(DATA) == 390


def test_day_19_part_2_ex_01():
    assert day_19.part_2(EXAMPLE1) == 3621


def test_day_19_part_2_solution():
    assert day_19.part_2(DATA) == 13327
