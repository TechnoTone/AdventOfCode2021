import utils
import day_01

TEST_INPUT = '199\n200\n208\n210\n200\n207\n240\n269\n260\n263'
TEST_DATA = utils.Input.test(TEST_INPUT).ints()

DATA = utils.Input.day(1).ints()


def test_day_01_part_1_ex_01():
    assert day_01.part_1(TEST_DATA) == 7


def test_day_01_part_1_solution():
    assert day_01.part_1(DATA) == 1602


def test_day_01_part_2_ex_01():
    assert day_01.part_2(TEST_DATA) == 5


def test_day_01_part_2_solution():
    assert day_01.part_2(DATA) == 1633
