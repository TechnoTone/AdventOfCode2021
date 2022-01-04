def part_1(field: list) -> int:
    count = 0

    while True:
        count += 1
        new_field = move(field)

        if new_field == field:
            return count

        field = new_field


def move(field: list) -> list:
    def mv(herd, d):
        moved = []
        for line in herd:
            first = line[0]
            s = (line + first).replace(d + ".", "." + d)
            if first == ".":
                moved.append(s[-1] + s[1:-1])
            else:
                moved.append(s[:-1])
        return moved

    def transpose(herd):
        return ["".join(line) for line in zip(*herd)]

    return transpose(mv(transpose(mv(field, ">")), "v"))
