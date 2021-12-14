from typing import Tuple


def part_1(input: list) -> int:
    numbers, boards = parseInput(input)
    return play(numbers, boards, True)


def part_2(input: list) -> int:
    numbers, boards = parseInput(input)
    return play(numbers, boards, False)


def parseInput(input: list) -> Tuple[list, list]:
    numbers = list(map(int, input[0].split(",")))
    boards = []
    for n in range(2, len(input), 6):
        boards.append(parseBoard(input[n : n + 5]))

    return numbers, boards


def parseBoard(input: list) -> Tuple[list, list]:
    rows = []
    cols = [[], [], [], [], []]

    for line in input:
        row = list(map(int, line.split()))
        for i in range(len(row)):
            cols[i].append(row[i])
        rows.append(row)

    return rows, cols


def play(numbers: list, boards: list, findFirst=True) -> int:
    for num in numbers:
        for b in range(len(boards)):
            for i in [0, 1]:
                for j in range(5):
                    if num in boards[b][i][j]:
                        boards[b][i][j].remove(num)

        for board in boards:
            score = boardScore(board)
            if score > 0:
                if findFirst or len(boards) == 1:
                    return score * num
                boards.remove(board)

    return 0


def boardScore(board) -> int:
    rows, cols = board
    if list(filter(lambda x: not x, rows + cols)):
        return sumRemaining(rows)

    return 0


def sumRemaining(lists: list) -> int:
    return sum(sum(lists, []))
