import day_12
from utils import Input

EXAMPLE1 = Input.ex(12, 1).lines()
EXAMPLE2 = Input.ex(12, 2).lines()
DATA = Input.day(12).lines()


def test_day_12_part_1_ex_01():
    assert day_12.part_1(EXAMPLE1) == 10


def test_day_12_part_1_ex_02():
    assert day_12.part_1(EXAMPLE2) == 19


def test_day_12_part_1_solution():
    assert day_12.part_1(DATA) == 4573


def test_day_12_part_2_ex_01():
    assert day_12.part_2(EXAMPLE1) == 36


def test_day_12_part_2_ex_02():
    assert day_12.part_2(EXAMPLE2) == 103


def test_day_12_part_2_solution():
    assert day_12.part_2(DATA) == 117509
