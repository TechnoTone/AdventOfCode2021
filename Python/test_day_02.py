from utils import Input
import day_02

TEST_INPUT = 'forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2'
TEST_DATA = Input.test(TEST_INPUT).lines()

DATA = Input.day(2).lines()


def test_day_02_part_1_ex_01():
    assert day_02.part_1(TEST_DATA) == 150


def test_day_02_part_1_solution():
    assert day_02.part_1(DATA) == 1893605


def test_day_02_part_2_ex_01():
    assert day_02.part_2(TEST_DATA) == 900


def test_day_02_part_2_solution():
    assert day_02.part_2(DATA) == 2120734350
