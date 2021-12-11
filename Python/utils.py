class Input:
    def __init__(self, data):
        self.__data = data

    @classmethod
    def test(cls, data: str):
        return cls(data)

    @classmethod
    def ex(cls, day: int, ex: int):
        with open(f"input/day_{day:02}_ex_{ex:02}.txt") as f:
            return cls(f.read())

    @classmethod
    def day(cls, day: int):
        with open(f"input/day_{day:02}.txt") as f:
            return cls(f.read())

    def __repr__(self):
        return f"Input: {self.__data}"

    def raw(self) -> str:
        return self.__data

    def lines(self) -> list:
        return list(self.__data.splitlines())

    def linesOfInts(self) -> list:
        return list(map(int, self.lines()))

    def linesOfDigits(self) -> list:
        return list(map(self.digits, self.lines()))

    def digits(self, input: str) -> list:
        return list(map(int, input))

    def ints(self) -> list:
        return list(map(int, self.__data.split(",")))
