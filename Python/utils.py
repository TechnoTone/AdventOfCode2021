class Input:

    def __init__(self, data):
        self.data = data

    @classmethod
    def test(cls, data: str):
        return cls(data)

    @classmethod
    def day(cls, day: int):
        with open(f'input/day{day}.txt') as f:
            return cls(f.read())

    def __repr__(self):
        return f'Input: {self.data}'

    def raw(self) -> str:
        return self.data

    def lines(self) -> list:
        return list(self.data.splitlines())

    def ints(self) -> list:
        return list(map(int, self.lines()))
