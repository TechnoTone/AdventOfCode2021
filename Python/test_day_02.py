from utils import Input
import day_02

EXAMPLE = Input.ex(2, 1).lines()
DATA = Input.day(2).lines()


def test_day_02_part_1_ex_01():
    assert day_02.part_1(EXAMPLE) == 150


def test_day_02_part_1_solution():
    assert day_02.part_1(DATA) == 1893605


def test_day_02_part_2_ex_01():
    assert day_02.part_2(EXAMPLE) == 900


def test_day_02_part_2_solution():
    assert day_02.part_2(DATA) == 2120734350
