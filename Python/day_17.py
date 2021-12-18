def part_1(xs: tuple, ys: tuple) -> int:
    return max(get_velocities(xs, ys).values())


def part_2(xs: tuple, ys: tuple) -> int:
    return len(get_velocities(xs, ys))


def get_velocities(xs, ys) -> dict:
    # potential x velocities
    possible_vx = []
    for vx in range(1, xs[1] + 1):
        v = vx
        x = 0
        while v > 0 and x < xs[0]:
            x += v
            v -= 1
        if xs[0] <= x <= xs[1]:
            possible_vx.append(vx)

    def in_zone(loc) -> bool:
        (x, y) = loc
        return xs[0] <= x <= xs[1] and ys[0] <= y <= ys[1]

    def step(loc, v) -> tuple:
        drag = -1 if v[0] > 0 else 0
        return (tuple(map(sum, zip(loc, v))), tuple(map(sum, zip(v, (drag, -1)))))

    possible_velocities = dict()
    for vx in possible_vx:

        # test y velocities
        for vy in range(-75, 75):  # used trial-and-error to narrow down this range
            loc = (0, 0)
            v = (vx, vy)
            height = 0
            while loc[0] < xs[0]:
                loc, v = step(loc, v)
                height = max(height, loc[1])
            while loc[0] <= xs[1] and loc[1] >= ys[0]:
                if in_zone(loc):
                    possible_velocities[(vx, vy)] = height
                loc, v = step(loc, v)
                height = max(height, loc[1])

    return possible_velocities
