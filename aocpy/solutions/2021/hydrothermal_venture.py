from aocpy.base import BaseSolution
from aocpy.utils.vec2 import Vec2


class HydrothermalVenture(BaseSolution, year=2021, day=5):
    def prepare(self, line: str) -> tuple[Vec2, Vec2]:
        return tuple(
            map(lambda x: Vec2(*list(map(int, x.strip().split(",")))), line.split("->"))
        )

    def get_overlaps(self, inputs: list[tuple[Vec2, Vec2]], diagonals: bool):
        total_overlaps = 0
        points = set()
        marked = set()
        for (left, right) in inputs:
            if not diagonals and left.x != right.x and left.y != right.y:
                continue
            line = left.get_line(right)
            for point in line:
                if point in points:
                    if point not in marked:
                        total_overlaps += 1
                        marked.add(point)
                    else:
                        continue
                else:
                    points.add(point)
        return total_overlaps

    def part1(self, inputs: list[tuple[Vec2, Vec2]]):
        return self.get_overlaps(inputs, False)

    def part2(self, inputs: list[tuple[Vec2, Vec2]]):
        return self.get_overlaps(inputs, True)
