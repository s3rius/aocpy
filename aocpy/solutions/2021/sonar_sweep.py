from aocpy.base import BaseSolution


class SonarSweep(BaseSolution, year=2021, day=1):
    def prepare(self, line: str) -> int:
        return int(line)

    def part1(self, inputs: list[int]):
        increases = 0
        for i in range(1, len(inputs)):
            if inputs[i] > inputs[i - 1]:
                increases += 1
        return increases

    def part2(self, inputs: list[int]):
        increases = 0
        for i in range(3, len(inputs)):
            if sum(inputs[i - 3 : i]) < sum(inputs[i - 2 : i + 1]):
                increases += 1
        return increases
