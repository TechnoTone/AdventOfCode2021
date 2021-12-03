from utils import Input
import day_03

TEST_INPUT = '00100\n11110\n10110\n10111\n10101\n01111\n00111\n11100\n10000\n11001\n00010\n01010'
TEST_DATA = Input.test(TEST_INPUT).lines()

DATA = Input.day(3).lines()


def test_day_03_part_1_ex_01():
    assert day_03.part_1(TEST_DATA) == 198


def test_day_03_part_1_solution():
    assert day_03.part_1(DATA) == 3959450


def test_day_03_part_2_ex_01():
    assert day_03.part_2(TEST_DATA) == 230


def test_day_03_part_2_solution():
    assert day_03.part_2(DATA) == 7440311
