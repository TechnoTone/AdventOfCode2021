from utils import Input
import day_04

EXAMPLE = Input.ex(4, 1).lines()
DATA = Input.day(4).lines()


def test_day_04_part_1_ex_01():
    assert day_04.part_1(EXAMPLE) == 4512


def test_day_04_part_1_solution():
    assert day_04.part_1(DATA) == 11774


def test_day_04_part_2_ex_01():
    assert day_04.part_2(EXAMPLE) == 1924


def test_day_04_part_2_solution():
    assert day_04.part_2(DATA) == 4495
