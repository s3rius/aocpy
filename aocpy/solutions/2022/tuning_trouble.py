from aocpy.base import BaseSolution


class TuningTrouble(BaseSolution, year=2022, day=6):
    def solve(self, inputs: int, buffer_len: int) -> int:
        line = inputs[0]
        buffer = []
        for i in range(len(line)):
            buffer.append(line[i])
            if len(buffer) == buffer_len:
                if len(set(buffer)) == buffer_len:
                    return i + 1
                buffer.pop(0)
        return "Heh"

    def part1(self, inputs: list[str]):
        return self.solve(inputs, buffer_len=4)

    def part2(self, inputs: list[str]):
        return self.solve(inputs, buffer_len=14)
