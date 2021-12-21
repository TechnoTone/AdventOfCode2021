from collections import Counter
from functools import lru_cache
from itertools import product


def part_1(positions: tuple) -> int:
    scores = [0, 0]
    dice = DeterministicDice()

    player = 1
    positions_ = list(positions)

    while max(scores) < 1000:
        player = 1 - player
        roll = dice.roll() + dice.roll() + dice.roll()
        positions_[player] += roll
        while positions_[player] > 10:
            positions_[player] -= 10
        scores[player] += positions_[player]
        pass

    return min(scores) * dice.rolls


def part_2(positions: tuple) -> int:
    return max(play(positions))


class DeterministicDice:
    def __init__(self):
        self.rolls = 0

    def roll(self):
        self.rolls += 1
        return (self.rolls - 1) % 100 + 1


rolls = Counter(sum(t) for t in product([1, 2, 3], repeat=3))


@lru_cache(maxsize=None)
def play(positions: tuple, scores: tuple = (0, 0), player: int = 0) -> int:

    wins = [0, 0]

    for throw, weight in rolls.items():
        positions_ = list(positions)
        scores_ = list(scores)

        positions_[player] = (positions_[player] + throw - 1) % 10 + 1
        scores_[player] += positions_[player]

        if scores_[player] >= 21:
            wins[player] += weight
        else:
            more_wins = play(tuple(positions_), tuple(scores_), 1 - player)
            wins[0] += more_wins[0] * weight
            wins[1] += more_wins[1] * weight

    return wins
