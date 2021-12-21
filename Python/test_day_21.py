import day_21
from utils import Input

EXAMPLE1 = (4, 8)
DATA = (10, 2)


def test_day_21_part_1_ex_01():
    assert day_21.part_1(EXAMPLE1) == 739785


def test_day_21_part_1_solution():
    assert day_21.part_1(DATA) == 916083


def test_day_21_part_2_ex_01():
    assert day_21.part_2(EXAMPLE1) == 444356092776315


def test_day_21_part_2_solution():
    assert day_21.part_2(DATA) == 49982165861983
