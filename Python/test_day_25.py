import day_25
from utils import Input

EXAMPLE1 = Input.ex(25, 1).lines()
DATA = Input.day(25).lines()


def test_day_25_part_1_ex_01():
    assert day_25.part_1(EXAMPLE1) == 58


def test_day_25_part_1_solution():
    assert day_25.part_1(DATA) == 520
