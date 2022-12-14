from aocpy.base import BaseSolution
import json
from typing import Any


class DistressSignal(BaseSolution, year=2022, day=13):
    def compare(self, left, right):
        if isinstance(left, int) and isinstance(right, int):
            return left < right
        elif isinstance(left, list) and isinstance(right, list):
            for i in range(max(len(left), len(right))):
                if i >= len(right):
                    return False
                if i >= len(left):
                    return True
                if left[i] == right[i]:
                    continue
                return self.compare(left[i], right[i])
            return True
        if isinstance(left, int):
            left = [left]
        if isinstance(right, int):
            right = [right]
        return self.compare(left, right)

    def read_pairs(self, inputs: list[str]):
        pairs = [[]]
        for line in inputs:
            if line.strip() == "":
                pairs.append([])
                continue

            pairs[-1].append(json.loads(line.strip()))
        return pairs

    def flatten(self, pairs: list[list[Any]]):
        flat = []
        for pair in pairs:
            flat.extend(pair)
        return flat

    def part1(self, inputs: list[str]):
        pairs = self.read_pairs(inputs)
        ind_sum = 0
        for index, (left, right) in enumerate(pairs):
            if self.compare(left, right):
                ind_sum += index + 1
        return ind_sum

    def part2(self, inputs: list[str]):
        signals = self.flatten(self.read_pairs(inputs))
        signals.append([[2]])
        signals.append([[6]])
        for i in range(len(signals)):
            for j in range(0, len(signals) - i - 1):
                if not self.compare(signals[j], signals[j + 1]):
                    signals[j], signals[j + 1] = signals[j + 1], signals[j]

        result = 1
        for index, signal in enumerate(signals):
            if signal == [[2]] or signal == [[6]]:
                result *= index + 1

        return result
