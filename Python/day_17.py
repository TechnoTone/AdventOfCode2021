def part_1(xs, ys) -> int:
    return foo(xs, ys)


def part_2(input: list) -> int:
    return 0


def foo(xs, ys) -> int:
    # potential x velocities
    possible_vx = []
    for vx in range(xs[0], xs[1] + 1):
        v = 0
        while vx > 0:
            v += 1
            vx -= v
        if vx == 0:
            possible_vx.append(v)

    # testing y velocities
    possible_heights = []
    vy = 0
    last_vy = 0
    while True:
        vy += 1

        for vx in possible_vx:
            y = 0
            v = vy
            height = 0
            for _ in range(vx):
                y += v
                v -= 1
                height = max(height, y)
            while y > ys[1]:
                # this is crude and I feel like it should be possible to
                # overshoot the target area but it seems to work to yay!
                y += v
                v -= 1
                height = max(height, y)
            if ys[0] <= y <= ys[1]:
                possible_heights.append(height)
                last_vy = vy

        if 0 < last_vy < vy - 100:
            # keep searching until nothing better for 100 steps
            break

    return max(possible_heights)
