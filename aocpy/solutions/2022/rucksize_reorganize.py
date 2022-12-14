from aocpy.base import BaseSolution


class RucksackReorganization(BaseSolution, year=2022, day=3):
    def get_priority(self, char: str):
        subst = 38
        if char.islower():
            subst = 96
        return ord(char) - subst

    def part1(self, inp: list[str]):
        prior_sum = 0
        for line in inp:
            diff = set(line[: len(line) // 2]).intersection(line[len(line) // 2 :])
            for diff_ch in diff:
                prior_sum += self.get_priority(diff_ch)
        return prior_sum

    def part2(self, inputs: list[str]):
        prior_sum = 0
        for line_idx in range(2, len(inputs), 3):
            cmn = (
                set(inputs[line_idx - 2].strip())
                .intersection(inputs[line_idx - 1].strip())
                .intersection(inputs[line_idx].strip())
            )
            for diff_ch in cmn:
                prior_sum += self.get_priority(diff_ch)
        return prior_sum
