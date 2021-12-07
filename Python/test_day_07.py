import day_07
from utils import Input

EXAMPLE = Input.ex(7, 1).ints()
DATA = Input.day(7).ints()


def test_day_07_part_1_ex_01():
    assert day_07.part_1(EXAMPLE) == 37


def test_day_07_part_1_solution():
    assert day_07.part_1(DATA) == 343468


def test_day_07_part_2_ex_01():
    assert day_07.part_2(EXAMPLE) == 168


def test_day_07_part_2_solution():
    assert day_07.part_2(DATA) == 96086265
