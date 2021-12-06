import day_01
from utils import Input

EXAMPLE = Input.ex(1, 1).linesOfInts()
DATA = Input.day(1).linesOfInts()


def test_day_01_part_1_ex_01():
    assert day_01.part_1(EXAMPLE) == 7


def test_day_01_part_1_solution():
    assert day_01.part_1(DATA) == 1602


def test_day_01_part_2_ex_01():
    assert day_01.part_2(EXAMPLE) == 5


def test_day_01_part_2_solution():
    assert day_01.part_2(DATA) == 1633
