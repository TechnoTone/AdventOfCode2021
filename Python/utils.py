class Input:

    def __init__(self, data):
        self.__data = data

    @classmethod
    def test(cls, data: str):
        return cls(data)

    @classmethod
    def day(cls, day: int):
        with open(f'input/day{day}.txt') as f:
            return cls(f.read())

    def __repr__(self):
        return f'Input: {self.__data}'

    def raw(self) -> str:
        return self.__data

    def lines(self) -> list:
        return list(self.__data.splitlines())

    def ints(self) -> list:
        return list(map(int, self.lines()))
