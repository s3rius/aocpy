from dataclasses import dataclass


@dataclass
class Vec2:
    x: int = 0
    y: int = 0

    @classmethod
    def from_vec2(cls, o: "Vec2") -> "Vec2":
        return Vec2(
            x=o.x,
            y=o.y,
        )

    def __hash__(self) -> int:
        return hash(self.x) + hash(self.y)

    def __sub__(self, o) -> "Vec2":
        if not isinstance(o, Vec2):
            o = Vec2(
                x=o,
                y=o,
            )
        return Vec2(
            x=self.x - o.x,
            y=self.y - o.y,
        )

    def __add__(self, o) -> "Vec2":
        if not isinstance(o, Vec2):
            o = Vec2(
                x=o,
                y=o,
            )
        return Vec2(
            x=self.x + o.x,
            y=self.y + o.y,
        )

    def __gt__(self, o) -> bool:
        if not isinstance(o, Vec2):
            o = Vec2(
                x=o,
                y=o,
            )
        return self.x > o.x or self.y > o.y

    def __ge__(self, o) -> bool:
        if not isinstance(o, Vec2):
            o = Vec2(
                x=o,
                y=o,
            )
        return self.x >= o.x or self.y >= o.y

    def __lt__(self, o) -> bool:
        if not isinstance(o, Vec2):
            o = Vec2(
                x=o,
                y=o,
            )
        return self.x < o.x or self.y < o.y

    def __le__(self, o) -> bool:
        if not isinstance(o, Vec2):
            o = Vec2(
                x=o,
                y=o,
            )
        return self.x <= o.x or self.y <= o.y

    def __eq__(self, o) -> bool:
        if not isinstance(o, Vec2):
            o = Vec2(
                x=o,
                y=o,
            )
        return self.x == o.x and self.y == o.y

    def get_line(self, destination: "Vec2") -> list["Vec2"]:
        if self.x == destination.x:
            return [
                Vec2(x=self.x, y=y)
                for y in range(
                    min(self.y, destination.y), max(self.y, destination.y) + 1
                )
            ]
        elif self.y == destination.y:
            return [
                Vec2(x=x, y=self.y)
                for x in range(
                    min(self.x, destination.x), max(self.x, destination.x) + 1
                )
            ]

        delta_x = destination.x - self.x
        delta_y = destination.y - self.y

        delta_x -= 1 if delta_x < 0 else -1
        delta_y -= 1 if delta_y < 0 else -1

        return [
            Vec2(x=x, y=y)
            for x, y in zip(
                range(self.x, self.x + delta_x, -1 if delta_x < 0 else 1),
                range(self.y, self.y + delta_y, -1 if delta_y < 0 else 1),
            )
        ]

    def __abs__(self) -> "Vec2":
        return Vec2(x=abs(self.x), y=abs(self.y))
