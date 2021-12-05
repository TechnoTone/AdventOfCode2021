from utils import Input
import day_03

EXAMPLE = Input.ex(3, 1).lines()
DATA = Input.day(3).lines()


def test_day_03_part_1_ex_01():
    assert day_03.part_1(EXAMPLE) == 198


def test_day_03_part_1_solution():
    assert day_03.part_1(DATA) == 3959450


def test_day_03_part_2_ex_01():
    assert day_03.part_2(EXAMPLE) == 230


def test_day_03_part_2_solution():
    assert day_03.part_2(DATA) == 7440311
