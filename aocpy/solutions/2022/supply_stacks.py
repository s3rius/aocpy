from aocpy.base import BaseSolution
from dataclasses import dataclass


@dataclass
class Instruction:
    count: int
    source: int
    dest: int


class SuplyStacks(BaseSolution, year=2022, day=5):
    def read_box_definitions(self, inputs: list[str]) -> list[list[str]]:
        box_defs = []
        nums = None
        for line in inputs:
            if line.strip() == "":
                nums = box_defs.pop()
                break
            box_defs.append(line.rstrip("\n"))

        boxes = []

        for i, char in enumerate(nums):
            if char.strip() != "":
                boxes.append([])
                for line in box_defs:
                    if line[i].strip() != "":
                        boxes[-1].append(line[i])
                boxes[-1].reverse()

        return boxes

    def read_instructions(self, inputs: list[str]) -> list[Instruction]:
        box_def = True
        instructions = []
        for line in inputs:
            if line.strip() == "":
                box_def = False
                continue
            if not box_def:
                _, count, _, src, _, dest = line.split()
                instructions.append(
                    Instruction(
                        count=int(count),
                        source=int(src) - 1,
                        dest=int(dest) - 1,
                    )
                )
        return instructions

    def solve(self, inputs: list[str], many_at_once=False) -> str:
        boxes = self.read_box_definitions(inputs)
        instructions = self.read_instructions(inputs)
        for instr in instructions:
            moveables = []
            for _ in range(instr.count):
                moveables.append(boxes[instr.source].pop())
            if many_at_once:
                moveables.reverse()
            boxes[instr.dest].extend(moveables)
        tops = []
        for cols in boxes:
            tops.append(cols[-1])
        return "".join(tops)

    def part1(self, inputs: list[str]):
        return self.solve(inputs, many_at_once=False)

    def part2(self, inputs: list[str]):
        return self.solve(inputs, many_at_once=True)
