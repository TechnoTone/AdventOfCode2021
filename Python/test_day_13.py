import day_13
from utils import Input

EXAMPLE1 = Input.ex(13, 1).lines()
DATA = Input.day(13).lines()


def test_day_13_part_1_ex_01():
    assert day_13.part_1(EXAMPLE1) == 17


def test_day_13_part_1_solution():
    assert day_13.part_1(DATA) == 765


def test_day_13_part_2_ex_01():
    output = day_13.part_2(EXAMPLE1)
    assert output[0] == "#####"
    assert output[1] == "#...#"
    assert output[2] == "#...#"
    assert output[3] == "#...#"
    assert output[4] == "#####"


def test_day_13_part_2_solution():
    output = day_13.part_2(DATA)  # RZKZLPGH
    assert output[0] == "###..####.#..#.####.#....###...##..#..#"
    assert output[1] == "#..#....#.#.#.....#.#....#..#.#..#.#..#"
    assert output[2] == "#..#...#..##.....#..#....#..#.#....####"
    assert output[3] == "###...#...#.#...#...#....###..#.##.#..#"
    assert output[4] == "#.#..#....#.#..#....#....#....#..#.#..#"
    assert output[5] == "#..#.####.#..#.####.####.#.....###.#..#"
