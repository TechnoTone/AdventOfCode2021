import day_17


def test_day_17_part_1_ex_01():
    xs = (20, 30)
    ys = (-10, -5)
    assert day_17.part_1(xs, ys) == 45


def test_day_17_part_1_solution():
    xs = (281, 311)
    ys = (-74, -54)
    assert day_17.part_1(xs, ys) == 2701


# def test_day_17_part_2_ex_01():
#     xs = (20, 30)
#     ys = (-10, -5)
#     assert day_17.part_2(xs, ys) == 112


# def test_day_17_part_2_solution():
#     xs = (281, 311)
#     ys = (-74, -54)
#     assert day_17.part_2(xs, ys) == 0
