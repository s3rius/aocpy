from aocpy.base import BaseSolution
from typing import Any


class CalorieCounting(BaseSolution, year=2022, day=1):
    def get_all_callories(self, inputs: list[str]) -> list[int]:
        calories = []
        buffer = 0
        for line in inputs:
            if line.strip() == "":
                calories.append(buffer)
                buffer = 0
                continue
            buffer += int(line.strip())
        return calories

    def part1(self, inp: list[str]) -> Any:
        cals = self.get_all_callories(inp)
        cals.sort(reverse=True)
        return cals[0]

    def part2(self, inp: list[str]) -> Any:
        cals = self.get_all_callories(inp)
        cals.sort(reverse=True)
        return sum(cals[:3])
