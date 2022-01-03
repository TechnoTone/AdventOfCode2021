import day_23
from utils import Input

EXAMPLE1 = Input.ex(23, 1).lines()
DATA = Input.day(23).lines()


def hallway(s):
    return [c.strip() for c in list(s)]


def rooms(s):
    n = len(s) // 4
    return tuple(s[i : i + n] for i in range(0, len(s), n))


def burrow(s):
    h = s[:11]
    r = rooms(s[11:])
    return (h, r)


def burrow_str(burrow) -> str:
    (hallway, rooms) = burrow
    return "".join(hallway) + "".join(c for r in rooms for c in r)


def get_moves(start):
    b = burrow(start[0])
    return [(burrow_str(bw), score) for (bw, score) in day_23.get_moves(b)]


class Test_get_moves:
    def test_when_already_solved(self):
        result = day_23.get_moves(burrow("...........AABBCCDD"))
        assert len(result) == 0
        result = day_23.get_moves(burrow("............A.B.C.D"))
        assert len(result) == 0

    def test_two_rooms_that_need_emptying(self):
        result = day_23.get_moves(burrow("...........BAABCCDD"))
        assert len(result) == 14
        assert sum(r[1] for r in result) == 370

    def test_four_rooms_that_need_emptying(self):
        result = day_23.get_moves(burrow("...........DDCCBBAA"))
        assert len(result) == 28
        assert sum(r[1] for r in result) == 37334

    def test_rooms_need_emptying_from_further_inside(self):
        result = day_23.get_moves(burrow("............B.A.C.D"))
        assert len(result) == 14
        assert sum(r[1] for r in result) == 447

    def test_rooms_once_emptied_can_be_moved_into(self):
        result = day_23.get_moves(burrow(".A..........BABCCDD"))
        assert len(result) == 10
        assert sum(r[1] for r in result) == 376

    def test_part_1_step_by_step(self):
        solution = [
            ("...........BACDBCDA", 0),  # 0
            ("...B.......BACD.CDA", 40),  # 40
            ("...B.......BA.DCCDA", 400),  # 440
            (".....D.....BA.BCCDA", 3030),  # 3470
            (".....D......ABBCCDA", 40),  # 3510
            (".....D.D....ABBCC.A", 2000),  # 5510
            ("...........AABBCCDD", 7011),  # 12521
        ]

        for n in range(len(solution) - 1):
            result = get_moves(solution[n])
            expected = solution[n + 1]
            assert expected in result, f"n = {n} : {expected}"

    def test_part_2_step_by_step(self):
        solution = [
            ("...........BDDACCBDBBACDACA", 0),  # 0
            ("..........DBDDACCBDBBAC.ACA", 3000),  # 3000
            ("A.........DBDDACCBDBBAC..CA", 10),  # 3010
            ("A........BDBDDACCBD.BAC..CA", 40),  # 3050
            ("A......B.BDBDDACCBD..AC..CA", 30),  # 3080
            ("AA.....B.BDBDDACCBD...C..CA", 8),  # 3088
            ("AA.....B.BDBDDA.CBD..CC..CA", 600),  # 3688
            ("AA.....B.BDBDDA..BD.CCC..CA", 600),  # 4288
            ("AA...B.B.BDBDDA...D.CCC..CA", 40),  # 4328
            ("AA.D......DBDDA.BBB.CCC..CA", 5180),  # 9508
            ("AA.D......DBDDA.BBBCCCC...A", 600),  # 10108
            ("AA.......ADBDDA.BBBCCCC...D", 9005),  # 19113
            ("AA.......AD.DDABBBBCCCC...D", 40),  # 19153
            ("AA.......AD..DABBBBCCCC..DD", 11000),  # 30153
            ("...........AAAABBBBCCCCDDDD", 14016),  # 44169
        ]

        for n in range(len(solution) - 1):
            result = get_moves(solution[n])
            expected = solution[n + 1]
            assert expected in result, f"n = {n} : {expected}"


def test_day_23_part_1_example_01():
    assert day_23.part_1(EXAMPLE1) == 12521


def test_day_23_part_1_solution():
    assert day_23.part_1(DATA) == 18300


def test_day_23_part_2_example_01():
    assert day_23.part_2(EXAMPLE1) == 44169


def test_day_23_part_2_solution():
    assert day_23.part_2(DATA) == 50190
