from aocpy.base import BaseSolution
from collections import Counter


class BinaryDiagnostic(BaseSolution, year=2021, day=3):
    def part1(self, inputs: list[str]):
        counters = [Counter() for _ in range(len(inputs[0].strip()))]
        for line in inputs:
            for idx, ch in enumerate(line.strip()):
                counters[idx][ch] += 1
        gamma = []
        epsilon = []
        for idx, counter in enumerate(counters):
            ch, _ = counter.most_common(1)[0]
            if ch == "0":
                inv = "1"
            else:
                inv = "0"
            gamma.append(ch)
            epsilon.append(inv)

        return int("".join(gamma), base=2) * int("".join(epsilon), base=2)

    def filter_by_bits(self, inputs: list[str], most_common: bool):
        current_pos = 0
        values = list(map(lambda x: x.strip(), inputs[:]))

        while len(values) > 1:
            counter = Counter()
            for line in values:
                counter[line[current_pos]] += 1

            common_char, _ = counter.most_common(1)[0]
            if counter["0"] == counter["1"]:
                common_char = "1"
            new_values = []
            for i in range(len(values)):
                if most_common and values[i][current_pos] == common_char:
                    new_values.append(values[i])
                elif not most_common and values[i][current_pos] != common_char:
                    new_values.append(values[i])

            values = new_values
            current_pos += 1
        return values[0]

    def part2(self, inputs: list[str]):
        return int(self.filter_by_bits(inputs, most_common=True), base=2) * int(
            self.filter_by_bits(inputs, most_common=False), base=2
        )
