def part_1(input: list) -> int:
    caves = parse(input)
    return pathCount(caves, "start", [], False)


def part_2(input: list) -> int:
    caves = parse(input)
    return pathCount(caves, "start", [], True)


def parse(input: list) -> dict:
    result = {}
    for line in input:
        [a, b] = line.split("-")

        if b != "start":
            if a in result:
                result[a].append(b)
            else:
                result[a] = [b]

        if a != "start" and b != "end":
            if b in result:
                result[b].append(a)
            else:
                result[b] = [a]

    return result


def pathCount(caves: dict, location: str, route: list, allowRepeat: bool) -> int:
    if location == "end":
        return 1

    if location.islower() and location in route:
        if allowRepeat:
            allowRepeat = False
        else:
            return 0

    route.append(location)

    count = 0
    for next in caves[location]:
        count += pathCount(caves, next, route.copy(), allowRepeat)

    return count
