from aocpy.base import BaseSolution
from aocpy.utils.vec2 import Vec2


class RegolithReservoir(BaseSolution, year=2022, day=14):
    def prepare(self, line: str) -> list[Vec2]:
        return list(
            map(
                lambda x: Vec2(*list(map(int, x.strip().split(",")))),
                line.strip().split("->"),
            )
        )

    def get_rock_positions(self, inputs: list[list[Vec2]]) -> set[Vec2]:
        obstacles = set()
        for points in inputs:
            previous_point = points[0]
            for idx in range(1, len(points)):
                obstacles.update(previous_point.get_line(points[idx]))
                previous_point = points[idx]
        return obstacles

    def draw_picture(
        self,
        obstacles: set[Vec2],
        sand_source: Vec2,
        sand_tiles: set[Vec2],
    ) -> None:
        max_y = 10
        for obstacle in obstacles:
            if obstacle.y > max_y:
                max_y = obstacle.y
        xs = set(map(lambda x: x.x, list(obstacles)))
        for y in range(max_y + 2):
            for x in range(min(xs) - 2, max(xs) + 3):
                current_point = Vec2(x=x, y=y)
                if current_point in obstacles:
                    ch = "#"
                elif current_point == sand_source:
                    ch = "+"
                elif current_point in sand_tiles:
                    ch = "o"
                else:
                    ch = "."
                print(ch, end="")
            print()

    def simulate_sand_grain(
        self,
        sand_grain: Vec2,
        obstacles: set[Vec2],
        sand_tiles: set[Vec2],
        lowest_point: int,
        lowest_as_floor: bool = False,
    ) -> Vec2:
        can_move = True
        while can_move:
            if lowest_as_floor and sand_grain.y + 1 >= lowest_point:
                return sand_grain
            if sand_grain.y > lowest_point:
                return None
            down = sand_grain + Vec2(0, 1)
            left = sand_grain + Vec2(-1, 1)
            right = sand_grain + Vec2(1, 1)
            if down not in obstacles and down not in sand_tiles:
                sand_grain = down
                continue
            if left not in obstacles and left not in sand_tiles:
                sand_grain = left
                continue
            if right not in obstacles and right not in sand_tiles:
                sand_grain = right
                continue
            can_move = False
        return sand_grain

    def solution(
        self,
        obstacles: set[Vec2],
        sand_source: Vec2,
        lowest_point: int,
        with_floor: bool,
    ) -> int:
        sand_tiles = set()
        i = 0
        while True:
            sand_grain = Vec2.from_vec2(sand_source)
            new_position = self.simulate_sand_grain(
                sand_grain=sand_grain,
                obstacles=obstacles,
                sand_tiles=sand_tiles,
                lowest_point=lowest_point,
                lowest_as_floor=with_floor,
            )
            if new_position is None:
                break
            if new_position == sand_source:
                break
            sand_tiles.add(new_position)
            i += 1
        self.draw_picture(
            obstacles=obstacles,
            sand_source=sand_source,
            sand_tiles=sand_tiles,
        )
        return i

    def part1(self, inputs: list[list[Vec2]]):
        obstacles = self.get_rock_positions(inputs)
        lowest_point = max(list(map(lambda x: x.y, list(obstacles)))) - 1
        return self.solution(
            obstacles=obstacles,
            sand_source=Vec2(500, 0),
            lowest_point=lowest_point,
            with_floor=False,
        )

    def part2(self, inputs: list[list[Vec2]]):
        obstacles = self.get_rock_positions(inputs)
        lowest_point = max(list(map(lambda x: x.y, list(obstacles)))) + 2
        return (
            self.solution(
                obstacles=obstacles,
                sand_source=Vec2(500, 0),
                lowest_point=lowest_point,
                with_floor=True,
            )
            + 1
        )
