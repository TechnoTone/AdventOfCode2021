from heapq import heapify, heappop, heappush
import sys


EXPECTED_OCCUPANT = ["A", "B", "C", "D"]
POD_HOME = {"A": 0, "B": 1, "C": 2, "D": 3}
MOVE_COST = {"A": 1, "B": 10, "C": 100, "D": 1000}
ROOM_POSITIONS = [2, 4, 6, 8]


def part_1(input: list) -> int:
    burrow = parse_burrow(input)
    return solve(burrow)


def part_2(input: list) -> int:
    input.insert(3, "  #D#C#B#A#")
    input.insert(4, "  #D#B#A#C#")
    burrow = parse_burrow(input)
    return solve(burrow)


def parse_burrow(input):
    hallway = input[1][1:12]
    rooms = ["", "", "", ""]
    for line in input[2:-1]:
        for r in range(4):
            rooms[r] += line[ROOM_POSITIONS[r] + 1]
    return (hallway, tuple(rooms))


def solve(burrow) -> int:
    queue = [(0, burrow)]
    heapify(queue)

    visited = set()
    best_score = sys.maxsize

    while queue:
        (score, burrow) = heappop(queue)

        if burrow in visited or score > best_score:
            continue

        visited.add(burrow)

        for (new_burrow, cost) in get_moves(burrow):
            if new_burrow not in visited:
                if solved(new_burrow):
                    if best_score > score + cost:
                        best_score = score + cost
                heappush(queue, (score + cost, new_burrow))
            else:
                pass

    return best_score


def solved(burrow) -> bool:
    return all(map(lambda h: h == ".", burrow[0]))


def z(s, i, c):
    return s[:i] + c + s[i + 1 :]


def zz(t, i, s):
    return t[:i] + (s,) + t[i + 1 :]


def get_moves(burrow) -> list:
    (hallway, rooms) = burrow
    moves = []

    for r_num, room in enumerate(rooms):
        if room_needs_emptying(r_num, room):
            pod, cost, room = remove_pod_from_room(room)
            h_room = ROOM_POSITIONS[r_num]
            for h in reachable_hallways(hallway, h_room):
                new_hallway = z(hallway, h, pod)
                new_rooms = zz(rooms, r_num, room)
                new_cost = cost + MOVE_COST[pod] * abs(h_room - h)

                x_burrow, x_cost = get_move_home(new_hallway, new_rooms)
                while x_burrow:
                    new_cost += x_cost
                    (new_hallway, new_rooms) = x_burrow
                    x_burrow, x_cost = get_move_home(new_hallway, new_rooms)

                moves.append(((new_hallway, new_rooms), new_cost))

    return moves


def room_is_complete(r_num, room):
    eo = EXPECTED_OCCUPANT[r_num]
    return all(map(lambda r: r == eo, room))


def room_is_available(r_num, room):
    return all(map(lambda r: r == "." or r == EXPECTED_OCCUPANT[r_num], room))


def room_needs_emptying(r_num, room):
    return any(map(lambda r: r != "." and r != EXPECTED_OCCUPANT[r_num], room))


def room_is_home(r_num, pod):
    return EXPECTED_OCCUPANT[r_num] == pod


def remove_pod_from_room(room):
    for p, pod in enumerate(room):
        if pod != ".":
            cost = MOVE_COST[pod] * (p + 1)
            return (pod, cost, z(room, p, "."))


def add_pod_to_room(room, pod):
    pos = room.count(".") - 1
    return (z(room, pos, pod), (pos + 1) * MOVE_COST[pod])


def reachable_hallways(hallway, start):
    h = start
    while h > 0:
        h -= 1
        if h in ROOM_POSITIONS:
            continue
        if hallway[h] == ".":
            yield h
        else:
            break

    h = start
    while h < len(hallway) - 1:
        h += 1
        if h in ROOM_POSITIONS:
            continue
        if hallway[h] == ".":
            yield h
        else:
            break


def get_move_home(hallway, rooms):
    for h, pod in enumerate(hallway):
        if pod == ".":
            continue

        dest_room_num = POD_HOME[pod]
        dest_room_pos = ROOM_POSITIONS[dest_room_num]
        dest_room = rooms[dest_room_num]

        if room_is_available(dest_room_num, dest_room):
            if path_is_open(h, dest_room_pos, hallway):
                new_room, cost = add_pod_to_room(dest_room, pod)
                cost += abs(ROOM_POSITIONS[dest_room_num] - h) * MOVE_COST[pod]
                new_hallway = z(hallway, h, ".")
                new_rooms = zz(rooms, dest_room_num, new_room)
                return ((new_hallway, new_rooms), cost)

    return (None, None)


def path_is_open(start, end, hallway):
    if start < end:
        dx = 1
    else:
        dx = -1

    start += dx  # ignore start as that's where the pod is moving from

    while start != end:
        if hallway[start] != ".":
            return False
        start += dx

    return True
