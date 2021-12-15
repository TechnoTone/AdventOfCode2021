import day_15
from utils import Input

EXAMPLE1 = Input.ex(15, 1).linesOfDigits()
DATA = Input.day(15).linesOfDigits()


def test_day_15_part_1_ex_01():
    assert day_15.part_1(EXAMPLE1) == 40


def test_day_15_part_1_solution():
    assert day_15.part_1(DATA) == 435


def test_day_15_part_2_ex_01():
    assert day_15.part_2(EXAMPLE1) == 315


def test_day_15_part_2_solution():
    assert day_15.part_2(DATA) == 2842
