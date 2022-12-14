from aocpy.base import BaseSolution
from dataclasses import dataclass
from typing import Optional
import enum
from time import sleep


class Instruction(enum.Enum):
    ADDX = enum.auto()
    NOOP = enum.auto()


@dataclass
class Command:
    instr: Instruction
    arg: Optional[int] = None

    @property
    def cycles(self) -> int:
        if self.instr == Instruction.NOOP:
            return 1
        else:
            return 2

    @property
    def value(self) -> int:
        if self.instr == Instruction.NOOP:
            return 0
        else:
            return self.arg


class CathodeRayTube(BaseSolution[Command], year=2022, day=10):
    def prepare(self, line: str) -> Command:
        split = line.strip().split()
        if len(split) == 2:
            _, arg = split
            return Command(instr=Instruction.ADDX, arg=int(arg))
        return Command(instr=Instruction.NOOP)

    def part1(self, inputs: list[Command]):
        register = 1
        cycle_num = 0
        target_cycles = [20 + 40 * i for i in range(6)]
        result = 0
        for cmd in inputs:
            for _ in range(cmd.cycles):
                cycle_num += 1
                if cycle_num in target_cycles:
                    result += cycle_num * register
            register += cmd.value

        return result

    def part2(self, inputs: list[Command]):
        crt = [["." for _ in range(40)] for _ in range(6)]
        cycle_num = 0
        register = 0
        for cmd in inputs:
            for _ in range(cmd.cycles):
                symbol = "."
                pixel_idx = cycle_num % 40
                if pixel_idx in {register, register + 1, register + 2}:
                    symbol = "#"
                crt[cycle_num // 40][pixel_idx] = symbol
                cycle_num += 1
            register += cmd.value

        for line in crt:
            print("".join(line))

        return "See the image above."
