#!/usr/bin/env python

from os.path import exists
import sys, getopt


def main(argv):
    try:
        day = int(argv[0])

        prepare_day(day)

        if day < 1 or day > 25:
            raise ValueError

    except ValueError:
        print("Unexpected error:", sys.exc_info()[0])
        print("Usage: _init_day.py <day>")
        print("Day must be an integer between 1 and 25")

    except:
        print("Unexpected error:", sys.exc_info()[0])
        print("Usage: _init_day.py <day>")
        sys.exit(2)


def prepare_day(day: int):
    print("Preparing day", day)
    createFile(f"input/day_{day:02}.txt", "")
    createFile(f"input/day_{day:02}_ex_01.txt", "")
    createFile(
        f"day_{day:02}.py",
        "def part_1(input: list) -> int:\n"
        + "    return 0\n"
        + "\n"
        + "\n"
        + "def part_2(input: list) -> int:\n"
        + "    return 0\n",
    )
    createFile(
        f"test_day_{day:02}.py",
        f"import day_{day:02}\n"
        + "from utils import Input\n"
        + "\n"
        + f"EXAMPLE1 = Input.ex({day:02}, 1).lines()\n"
        + f"DATA = Input.day({day:02}).lines()\n"
        + "\n"
        + "\n"
        + f"def test_day_{day:02}_part_1_ex_01():\n"
        + f"    assert day_{day:02}.part_1(EXAMPLE1) == 0\n"
        + "\n"
        + "\n"
        + f"# def test_day_{day:02}_part_1_solution():\n"
        + f"#     assert day_{day:02}.part_1(DATA) == 0\n"
        + "\n"
        + "\n"
        + f"# def test_day_{day:02}_part_2_ex_01():\n"
        + f"#     assert day_{day:02}.part_2(EXAMPLE1) == 0\n"
        + "\n"
        + "\n"
        + f"# def test_day_{day:02}_part_2_solution():\n"
        + f"#     assert day_{day:02}.part_2(DATA) == 0\n"
        + "\n",
    )


def createFile(filepath, contents):
    if not exists(filepath):
        with open(filepath, "a") as f:
            f.write(contents)
            f.close()


if __name__ == "__main__":
    main(sys.argv[1:])
