import day_09
from utils import Input

EXAMPLE = Input.ex(9, 1).lines()
DATA = Input.day(9).lines()


def test_day_09_part_1_ex_01():
    assert day_09.part_1(EXAMPLE) == 15


def test_day_09_part_1_solution():
    assert day_09.part_1(DATA) == 518


def test_day_09_part_2_ex_01():
    assert day_09.part_2(EXAMPLE) == 1134


def test_day_09_part_2_solution():
    assert day_09.part_2(DATA) == 949905
