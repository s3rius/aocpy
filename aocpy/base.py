from pathlib import Path
from typing import Any


class BaseSolution:
    INPUT_PATH: Path
    TEST_INPUT_PATH: Path
    solutions: dict[int, "BaseSolution"] = {}
    _AOC_DAY: int
    _AOC_YEAR: int

    def __init_subclass__(cls, day: int, year: int, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        cls._AOC_DAY = day
        cls._AOC_YEAR = year
        cls.INPUT_PATH = Path(f"./inputs/{year}/{day}.txt")
        cls.TEST_INPUT_PATH = Path(f"./inputs/{year}/{day}_test.txt")
        cls.solutions[(year, day)] = cls()

    def part1(self, inputs: list[Any]):
        pass

    def part2(self, inputs: list[Any]):
        pass

    def prepare(self, line: str) -> Any:
        raise NotImplemented

    def run(self, test: bool = False):
        inputs = self.load_file(test)
        if inputs is None:
            return
        print()
        if self.__class__.prepare != BaseSolution.prepare:
            inputs = list(map(self.prepare, inputs))
        if self.__class__.part1 != BaseSolution.part1:
            print(f"Part 1: {self.part1(inputs)}")
        if self.__class__.part2 != BaseSolution.part2:
            print(f"Part 2: {self.part2(inputs)}")

    def load_file(self, test: bool):
        file_path = self.INPUT_PATH
        if test:
            file_path = self.TEST_INPUT_PATH
            if not file_path.exists():
                print(
                    f"WARNING: {self.TEST_INPUT_PATH} doesn't exist. Running with real values.",
                )
                file_path = self.INPUT_PATH

        if not file_path.exists():
            print(f"{file_path} doesn't exist.")
            return None

        with open(file_path, "r") as f:
            print(f"Values file: {file_path}")
            return f.readlines()
