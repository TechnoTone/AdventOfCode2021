import day_11
from utils import Input

EXAMPLE1 = Input.ex(11, 1).linesOfDigits()
EXAMPLE2 = Input.ex(11, 2).linesOfDigits()
EXAMPLE3 = Input.ex(11, 3).linesOfDigits()
EXAMPLE4 = Input.ex(11, 4).linesOfDigits()
DATA = Input.day(11).linesOfDigits()


def test_day_11_part_1_steps():
    assert day_11.step(EXAMPLE1) == (9, EXAMPLE2)
    assert day_11.step(EXAMPLE2) == (0, EXAMPLE3)


def test_day_11_part_1_ex_04():
    assert day_11.part_1(EXAMPLE4) == 1656


def test_day_11_part_1_solution():
    assert day_11.part_1(DATA) == 1652


def test_day_11_part_2_ex_01():
    assert day_11.part_2(EXAMPLE4) == 195


def test_day_11_part_2_solution():
    assert day_11.part_2(DATA) == 220
