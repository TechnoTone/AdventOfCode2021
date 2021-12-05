from utils import Input
import day_05

EXAMPLE = Input.ex(5, 1).lines()
DATA = Input.day(5).lines()


def test_day_05_part_1_ex_01():
    assert day_05.part_1(EXAMPLE) == 5


def test_day_05_part_1_solution():
    assert day_05.part_1(DATA) == 5294


def test_day_05_part_2_ex_01():
    assert day_05.part_2(EXAMPLE) == 12


def test_day_05_part_2_solution():
    assert day_05.part_2(DATA) == 21698
