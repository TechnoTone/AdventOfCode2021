import day_14
from utils import Input

EXAMPLE1 = Input.ex(14, 1).lines()
DATA = Input.day(14).lines()


def test_day_14_part_1_ex_01_unoptimised():
    assert day_14.part_1_unoptimised(EXAMPLE1) == 1588


def test_day_14_part_1_solution_unoptimised():
    assert day_14.part_1_unoptimised(DATA) == 3048


def test_day_14_part_1_ex_01():
    assert day_14.part_1(EXAMPLE1) == 1588


def test_day_14_part_1_solution():
    assert day_14.part_1(DATA) == 3048


def test_day_14_part_2_ex_01():
    assert day_14.part_2(EXAMPLE1) == 2188189693529


def test_day_14_part_2_solution():
    assert day_14.part_2(DATA) == 3288891573057
