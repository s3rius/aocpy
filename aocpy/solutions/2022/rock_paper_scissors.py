from aocpy.base import BaseSolution



class RockPaperScissors(BaseSolution, year=2022, day=2):
    def prepare(self, line: str) -> tuple[str, str]:
        return tuple(line.split())

    def part1(self, inp: list[tuple[str, str]]):
        score = 0
        for (opp, you) in inp:
            score += {"X": 1, "Y": 2, "Z": 3}[you] + {
                ("A", "X"): 3,
                ("A", "Y"): 6,
                ("A", "Z"): 0,
                ("B", "X"): 0,
                ("B", "Y"): 3,
                ("B", "Z"): 6,
                ("C", "X"): 6,
                ("C", "Y"): 0,
                ("C", "Z"): 3,
            }[(opp, you)]

        return score

    def part2(self, inp: list[tuple[str, str]]):
        score = 0
        for opp, you in inp:
            score += {"X": 0, "Y": 3, "Z": 6}[you] + {
                ("A", "X"): 3,
                ("A", "Y"): 1,
                ("A", "Z"): 2,
                ("B", "X"): 1,
                ("B", "Y"): 2,
                ("B", "Z"): 3,
                ("C", "X"): 2,
                ("C", "Y"): 3,
                ("C", "Z"): 1,
            }[(opp, you)]

        return score
