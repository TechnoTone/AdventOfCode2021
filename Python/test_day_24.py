import day_24
from utils import Input

DATA = Input.day(24).lines()


def test_day_24_part_1_solution():
    assert day_24.part_1(DATA) == 99298993199873


def test_day_24_part_2_solution():
    assert day_24.part_2(DATA) == 73181221197111
