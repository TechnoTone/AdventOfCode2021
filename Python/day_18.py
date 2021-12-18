from functools import reduce
from itertools import permutations
import re


def part_1(input: list) -> int:
    return magnitude(sum_snailfish(input))


def part_2(input: list) -> int:
    def sum_and_reduce(options):
        return magnitude(sum_snailfish(options))

    return max(map(sum_and_reduce, permutations(input, 2)))


def reduce_once(input: str) -> str:
    parts = parse(input)
    d = 0

    def preceding_int(index: int) -> int:
        while index > 0:
            index -= 1
            if type(parts[index]) == int:
                return index

    def following_int(index: int) -> int:
        while index < len(parts) - 1:
            index += 1
            if type(parts[index]) == int:
                return index

    def parts_string() -> str:
        return "".join(map(str, parts))

    # explode
    for i in range(len(parts)):
        if type(parts[i]) == int:
            pass
        else:
            match parts[i]:
                case '[':
                    if d==4:
                        v1,_,v2 = parts[i+1:i+4]
                        del parts[i:i+4]
                        parts[i] = 0

                        ix = preceding_int(i)
                        if ix:
                            parts[ix] += v1

                        ix = following_int(i)
                        if ix:
                            parts[ix] += v2

                        # exploded a pair so stop and return
                        return parts_string()

                    d+=1
                case ']':
                    d-=1
                case ',':
                    pass

    for i in range(len(parts)):
        if type(parts[i]) == int:
            if parts[i] > 9:
                v = parts[i]
                v1 = v // 2
                v2 = v - v1
                parts = parts[:i] + ['[', v1, ',', v2, ']'] + parts[i+1:]
                return parts_string()

    return input


def full_reduce(input: str) -> str:
    while True:
        result = reduce_once(input)
        if result == input:
            return result
        input = result

def sum_snailfish(input:list) -> str:
    def sum_and_reduce(a,b):
        return full_reduce(f'[{a},{b}]')

    return reduce(sum_and_reduce, input)

def magnitude(input:str) -> int:
    parts = parse(input)

    while len(parts) > 1:
        i = 0
        while i < len(parts) - 1:
            if parts[i] == '[':
                v1,_,v2 = parts[i+1:i+4]
                if type(v1) == int == type(v2):
                    del parts[i:i+4]
                    parts[i] = v1 * 3 + v2 * 2
            i += 1

    return parts[0]

    
def parse(input: str) -> list:
    def parseint(s):
        return int(s) if s.isnumeric() else s
    return list(map(parseint, re.findall("\[|\]|,|\d+", input)))
