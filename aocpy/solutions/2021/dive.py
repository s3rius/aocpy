import enum
from dataclasses import dataclass

from aocpy.base import BaseSolution
from aocpy.utils.vec2 import Vec2


@enum.unique
class Direction(enum.Enum):
    UP = enum.auto()
    DOWN = enum.auto()
    FORWARD = enum.auto()


@dataclass
class Instruction:
    direction: Direction
    value: int


class Dive(BaseSolution, year=2021, day=2):
    def prepare(self, line: str) -> Instruction:
        direction, value = line.split()
        return Instruction(
            direction=Direction[direction.upper()],
            value=int(value),
        )

    def part1(self, inputs: list[Instruction]):
        position = Vec2()
        for instr in inputs:
            if instr.direction == Direction.DOWN:
                position.y += instr.value
            elif instr.direction == Direction.UP:
                position.y -= instr.value
            elif instr.direction == Direction.FORWARD:
                position.x += instr.value

        return position.x * position.y

    def part2(self, inputs: list[Instruction]):
        position = Vec2()
        aim = 0
        for instr in inputs:
            if instr.direction == Direction.DOWN:
                aim += instr.value
            elif instr.direction == Direction.UP:
                aim -= instr.value
            elif instr.direction == Direction.FORWARD:
                position.x += instr.value
                position.y += aim * instr.value

        return position.x * position.y
