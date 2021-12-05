from utils import Input
import day_05

TEST_INPUT = '0,9 -> 5,9\n8, 0 -> 0, 8\n9, 4 -> 3, 4\n2, 2 -> 2, 1\n7, 0 -> 7, 4\n6, 4 -> 2, 0\n0, 9 -> 2, 9\n3, 4 -> 1, 4\n0, 0 -> 8, 8\n5, 5 -> 8, 2'
TEST_DATA = Input.test(TEST_INPUT).lines()
DATA = Input.day(5).lines()


def test_day_05_part_1_ex_01():
    assert day_05.part_1(TEST_DATA) == 5


def test_day_05_part_1_solution():
    assert day_05.part_1(DATA) == 5294


def test_day_05_part_2_ex_01():
    assert day_05.part_2(TEST_DATA) == 12


def test_day_05_part_2_solution():
    assert day_05.part_2(DATA) == 21698
