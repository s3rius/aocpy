from aocpy.base import BaseSolution
from dataclasses import dataclass
from aocpy.utils.vec2 import Vec2
from typing import Optional


@dataclass
class Sensor:
    pos: Vec2
    beacon: Vec2


@dataclass
class Square:
    up: Vec2
    down: Vec2
    left: Vec2
    right: Vec2

    def get_edge(self) -> "Square":
        return Square(
            up=self.up + Vec2(0, 1),
            down=self.down - Vec2(0, 1),
            right=self.right + Vec2(1, 0),
            left=self.left - Vec2(1, 0),
        )


class BeaconExclusionZone(BaseSolution, year=2022, day=15):
    def prepare(self, line: str) -> Sensor:
        coords = list(
            map(
                lambda x: Vec2(*x),
                map(
                    lambda lne: list(
                        map(
                            lambda sym: int(sym.split("=")[1]),
                            lne.strip().split("at")[1].split(","),
                        )
                    ),
                    line.strip().split(":"),
                ),
            )
        )

        return Sensor(pos=coords[0], beacon=coords[1])

    def draw_picture(self, squares: list[Square]):
        min_y = min([sqr.down.y for sqr in squares])
        max_y = max([sqr.up.y for sqr in squares])
        min_x = min([sqr.left.x for sqr in squares])
        max_x = max([sqr.right.x for sqr in squares])
        points = set()
        for sqr in squares:
            points.update(
                sqr.up.get_line(sqr.left)
                + sqr.up.get_line(sqr.right)
                + sqr.down.get_line(sqr.left)
                + sqr.down.get_line(sqr.right)
            )

        for y in range(min_y - 2, max_y + 3):
            for x in range(min_x - 2, max_x + 3):
                if Vec2(x=x, y=y) in points:
                    ch = "x"
                elif Vec2(x=x, y=y) == Vec2(x=14, y=11):
                    ch = "#"
                else:
                    ch = "."
                print(ch, end="")
            print()

    def part1(self, sensors: list[Sensor]):
        TARGET_Y = 2_000_000
        covered_points = set()
        for sensor in sensors:
            distance_to_beacon = sensor.pos.manhattan_distance(sensor.beacon)
            distanct_to_target = abs(TARGET_Y - sensor.pos.y)
            if distance_to_beacon < distanct_to_target:
                continue
            for x in range(
                sensor.pos.x - (distance_to_beacon - distanct_to_target),
                sensor.pos.x + (distance_to_beacon - distanct_to_target),
            ):
                covered_points.add(Vec2(x=x, y=TARGET_Y))
        return len(covered_points)

    def part2(self, sensors: list[Sensor]):
        squares: "list[Square]" = []
        edges: "list[Square]" = []
        for sensor in sensors:
            radius = sensor.pos.manhattan_distance(sensor.beacon)
            squares.append(
                Square(
                    up=sensor.pos + Vec2(0, radius),
                    down=sensor.pos - Vec2(0, radius),
                    left=sensor.pos - Vec2(radius, 0),
                    right=sensor.pos + Vec2(radius, 0),
                )
            )
            edges.append(squares[-1].get_edge())
