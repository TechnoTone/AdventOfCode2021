import day_20
from utils import Input

EXAMPLE1 = Input.ex(20, 1).lines()
DATA = Input.day(20).lines()


def test_day_20_part_1_ex_01():
    assert day_20.part_1(EXAMPLE1) == 35


def test_day_20_part_1_solution():
    assert day_20.part_1(DATA) == 5395


def test_day_20_part_2_ex_01():
    assert day_20.part_2(EXAMPLE1) == 3351


def test_day_20_part_2_solution():
    assert day_20.part_2(DATA) == 17584
