import day_06
from utils import Input

EXAMPLE = Input.ex(6, 1).ints()
DATA = Input.day(6).ints()


day_06.part_1(EXAMPLE)


def test_day_06_part_1_ex_01():
    assert day_06.part_1(EXAMPLE) == 5934


def test_day_06_part_1_solution():
    assert day_06.part_1(DATA) == 361169


def test_day_06_part_2_ex_01():
    assert day_06.part_2(EXAMPLE) == 26984457539


def test_day_06_part_2_solution():
    assert day_06.part_2(DATA) == 1634946868992
