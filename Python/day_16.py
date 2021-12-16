from functools import reduce


def part_1(input: str) -> int:
    return Packet.from_str(input).sum_versions()


def part_2(input: list) -> int:
    return Packet.from_str(input).value


class Packet:
    def __init__(self, version: int, typeId: int, value: int, packets: list):
        self.version = version
        self.typeId = typeId
        self.value = value
        self.packets = packets

    def sum_versions(self) -> int:
        return self.version + sum(p.sum_versions() for p in self.packets)

    @classmethod
    def from_str(cls, input: str):
        bits = list(bin(int(input, 16))[2:].zfill(4 * len(input)))
        return cls.from_bits(bits)

    @classmethod
    def from_bits(cls, bits: list):
        def read(size: int = 1) -> str:
            s = bits[0:size]
            del bits[0:size]
            return "".join(s)

        def read_int(size: int) -> int:
            s = read(size)
            return int(s, 2)

        def read_value() -> int:
            result = ""
            while read() == "1":
                result += read(4)
            result += read(4)

            return int(result, 2)

        def product(x):
            return reduce(lambda a, b: a * b, x)

        def greater(x):
            return x[0] > x[1]

        def less(x):
            return x[0] < x[1]

        def equal(x):
            return x[0] == x[1]

        operations = [sum, product, min, max, None, greater, less, equal]

        version = read_int(3)
        typeId = read_int(3)
        packets = []

        if typeId == 4:
            value = read_value()
        else:
            if read() == "0":
                l = read_int(15)
                target_len = len(bits) - l
                while len(bits) > target_len:
                    packets.append(Packet.from_bits(bits))
            else:
                l = read_int(11)
                for _ in range(l):
                    packets.append(Packet.from_bits(bits))

            value = int(operations[typeId]([p.value for p in packets]))

        return cls(version, typeId, value, packets)
