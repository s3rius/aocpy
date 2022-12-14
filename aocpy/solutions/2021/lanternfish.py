from aocpy.base import BaseSolution
from functools import partial


class Lanternfish(BaseSolution, year=2021, day=6):
    def calc_latern(self, fishes: list[int], days: int = 80) -> int:
        cache = {}

        def lanternfib(num: int):
            if num in cache:
                return cache[num]
            if num < 1:
                return 1
            res = lanternfib(num - 7) + lanternfib(num - 9)
            cache[num] = res
            return res

        return sum(map(lambda x: lanternfib(days - x), fishes))

    def part1(self, inputs: list[str]):
        return self.calc_latern(list(map(int, inputs[0].strip().split(","))), 80)

    def part2(self, inputs: list[str]):
        return self.calc_latern(list(map(int, inputs[0].strip().split(","))), 256)
