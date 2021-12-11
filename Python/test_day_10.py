import day_10
from utils import Input

EXAMPLE = Input.ex(10, 1).lines()
DATA = Input.day(10).lines()


def test_day_10_part_1_ex_01():
    assert day_10.part_1(EXAMPLE) == 26397


def test_day_10_part_1_solution():
    assert day_10.part_1(DATA) == 316851


def test_day_10_part_2_ex_01():
    assert day_10.part_2(EXAMPLE) == 288957


def test_day_10_part_2_solution():
    assert day_10.part_2(DATA) == 2182912364
