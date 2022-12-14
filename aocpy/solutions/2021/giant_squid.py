from collections import defaultdict
from dataclasses import dataclass, field
from typing import DefaultDict

from aocpy.base import BaseSolution
from aocpy.utils.vec2 import Vec2


@dataclass
class Board:
    grid: list[list[int]]
    marks: list[Vec2] = field(default_factory=list)

    _cache: DefaultDict[int, list[Vec2]] = field(
        default_factory=lambda: defaultdict(list)
    )

    def is_winner(self):
        for i in range(5):
            if len(list(filter(lambda value: value.x == i, self.marks))) == 5:
                return True
            if len(list(filter(lambda value: value.y == i, self.marks))) == 5:
                return True
        return False

    def init_cache(self) -> None:
        for y, col in enumerate(self.grid):
            for x, val in enumerate(col):
                self._cache[val].append(Vec2(x=x, y=y))

    def check_number(self, val: int) -> bool:
        if len(self._cache[val]) > 0:
            self.marks.extend(self._cache[val])
            return True
        return False

    def calculate_score(self, last_number: int):
        marks = set(self.marks)
        unmarked_sum = 0
        for y, col in enumerate(self.grid):
            for x, val in enumerate(col):
                if Vec2(x=x, y=y) not in marks:
                    unmarked_sum += val
        return unmarked_sum * last_number


@dataclass
class Bingo:
    numbers: list[int]
    boards: list[Board]


class GiantSquid(BaseSolution, year=2021, day=4):
    def parse_bingo(self, inputs: list[str]):
        numbers = list(map(int, inputs[0].strip().split(",")))
        board_grids = [[]]
        for i in range(2, len(inputs)):
            line = inputs[i].strip()
            if line == "":
                board_grids.append([])
                continue
            board_grids[-1].append(list(map(int, line.split())))

        boards = []
        for grid in board_grids:
            board = Board(grid=grid)
            board.init_cache()
            boards.append(board)

        return Bingo(
            numbers=numbers,
            boards=boards,
        )

    def part1(self, inputs: list[str]):
        bingo = self.parse_bingo(inputs)

        for number in bingo.numbers:
            for board in bingo.boards:
                if board.check_number(number):
                    if board.is_winner():
                        return board.calculate_score(number)

    def part2(self, inputs: list[str]):
        bingo = self.parse_bingo(inputs)
        last_score = 0
        boards = bingo.boards
        for number in bingo.numbers:
            new_boards = []
            for board in boards:
                if board.check_number(number):
                    if board.is_winner():
                        last_score = board.calculate_score(number)
                        continue
                new_boards.append(board)
            boards = new_boards

        return last_score
