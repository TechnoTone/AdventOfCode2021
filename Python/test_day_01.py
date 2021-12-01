import utils
import day_01

TEST_INPUT = '199\n200\n208\n210\n200\n207\n240\n269\n260\n263'


def test_day_01_part_1_ex_01():
    assert day_01.part_1(TEST_INPUT) == 7


def test_day_01_part_1_solution():
    assert day_01.part_1(utils.read_input_file(1)) == 1602


def test_day_01_part_2_ex_01():
    assert day_01.part_2(TEST_INPUT) == 5


def test_day_01_part_2_solution():
    assert day_01.part_2(utils.read_input_file(1)) == 1633
