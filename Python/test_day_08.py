import day_08
from utils import Input

EXAMPLE = Input.ex(8, 1).lines()
DATA = Input.day(8).lines()


def test_day_08_part_1_ex_01():
    assert day_08.part_1(EXAMPLE) == 26


def test_day_08_part_1_solution():
    assert day_08.part_1(DATA) == 237


def test_day_08_value():
    line = day_08.parseLine(
        "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    )
    assert day_08.value(line) == 5353


def test_day_08_part_2_ex_01():
    assert day_08.part_2(EXAMPLE) == 61229


def test_day_08_part_2_solution():
    assert day_08.part_2(DATA) == 1009098
