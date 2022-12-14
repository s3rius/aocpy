from aocpy.base import BaseSolution
from dataclasses import dataclass
import enum
from aocpy.utils.vec2 import Vec2


def sign(value: int):
    if value > 0:
        return 1
    elif value == 0:
        return 0
    else:
        return -1


@enum.unique
class Direction(enum.Enum):
    U = "UP"
    L = "LEFT"
    R = "RIGHT"
    D = "DOWN"


@dataclass
class Look:
    direction: Direction
    value: int


class RopeBridge(BaseSolution[Look], year=2022, day=9):
    def prepare(self, line: str) -> Look:
        direction, value = line.split()
        return Look(direction=Direction[direction], value=int(value))

    def looks_to_vecs(self, inputs: list[Look]) -> list[Vec2]:
        vecs = []
        for look in inputs:
            if look.direction == Direction.U:
                head_move = Vec2(0, 1)
            elif look.direction == Direction.D:
                head_move = Vec2(0, -1)
            elif look.direction == Direction.L:
                head_move = Vec2(-1, 0)
            else:
                head_move = Vec2(1, 0)
            for _ in range(look.value):
                vecs.append(head_move)
        return vecs

    def get_path(self, head_moves: list[Vec2], rope_len: int) -> list[Vec2]:
        rope = [Vec2(0, 0) for _ in range(rope_len)]
        path = []
        for head_move in head_moves:
            for i in range(rope_len):
                if i == 0:
                    rope[i] = rope[i] + head_move
                    continue
                delta = rope[i - 1] - rope[i]
                if abs(delta) > Vec2(1, 1):
                    rope[i] += Vec2(
                        x=sign(delta.x),
                        y=sign(delta.y),
                    )

                if i == rope_len - 1:
                    path.append(rope[i])

        return path

    def part1(self, inputs: list[Look]):
        return len(set(self.get_path(self.looks_to_vecs(inputs), 2)))

    def part2(self, inputs: list[Look]):
        return len(set(self.get_path(self.looks_to_vecs(inputs), 10)))
