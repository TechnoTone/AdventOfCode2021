def part_1(input: list) -> int:
    return fish_2(input, 80)


def part_2(input: list) -> int:
    return fish_2(input, 256)


def fish_1(input: list, iterations: int) -> int:
    # First naive brute force solution
    # Worked ok for part 1 but was too slow for part 2
    for i in range(iterations):
        for j in range(len(list(filter(lambda n: n == 0, input)))):
            input.append(9)
        input = list(map(lambda n: n - 1 if n > 0 else 6, input))
    return len(input)


def fish_2(input: list, iterations: int) -> int:
    fishPopulation = list(map(lambda n: input.count(n), range(9)))
    for _ in range(iterations):
        newFishPopulation = [0] * 9
        for i in range(8):
            newFishPopulation[i] = fishPopulation[i + 1]
        newFishPopulation[6] += fishPopulation[0]
        newFishPopulation[8] = fishPopulation[0]
        fishPopulation = newFishPopulation

    return sum(fishPopulation)
