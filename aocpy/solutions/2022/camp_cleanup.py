from typing_extensions import TypeAlias

from aocpy.base import BaseSolution


class CampCleanup(BaseSolution, year=2022, day=4):
    def prepare(self, line: str) -> list[list[int]]:
        return list(map(lambda s: list(map(int, s.split("-"))), line.split(",")))

    def part1(self, inputs: list[list[list[int]]]):
        fully_conts = 0
        for (fst_l, fst_r), (snd_l, snd_r) in inputs:
            if snd_l <= fst_l <= snd_r and snd_l <= fst_r <= snd_r:
                fully_conts += 1
            elif fst_l <= snd_l <= fst_r and fst_l <= snd_r <= fst_r:
                fully_conts += 1

        return fully_conts

    def part2(self, inputs: list[list[list[int]]]):
        overlaps = 0
        for (fst_l, fst_r), (snd_l, snd_r) in inputs:
            if snd_l <= fst_l <= snd_r or snd_l <= fst_r <= snd_r:
                overlaps += 1
            elif fst_l <= snd_l <= fst_r or fst_l <= snd_r <= fst_r:
                overlaps += 1

        return overlaps
