import inspect
from pathlib import Path

from typer import Typer

from aocpy.base import BaseSolution
from aocpy.solutions import load_all_solutions
import requests
from aocpy.settings import settings
import re

cli = Typer()


@cli.command()
def run(
    year: int,
    day: int,
    test: bool = False,
):
    load_all_solutions()
    try:
        solution = BaseSolution.solutions[(year, day)]
    except LookupError:
        print(f"Solution for {year}:{day} cannot be found.")
        return 1

    solution_path = Path(inspect.getfile(solution.__class__)).relative_to(
        Path(__file__).parent,
    )
    print(f"Running solution from file: {solution_path}")
    solution.run(test)


@cli.command(name="list")
def list_solved(year: int):
    load_all_solutions()
    solutions = []
    for solution in BaseSolution.solutions.values():
        if solution._AOC_YEAR == year:
            solutions.append(solution)
    solutions.sort(key=lambda sol: sol._AOC_DAY)
    for sol in solutions:
        sol_path = Path(inspect.getfile(sol.__class__)).relative_to(
            Path(__file__).parent,
        )
        print(f"day {sol._AOC_DAY}:", sol_path)


@cli.command(name="prepare")
def prepare(year: int, day: int):
    page = requests.get(f"https://adventofcode.com/{year}/day/{day}")
    name = re.search(rf"--- Day {day}: (?P<name>.*) ---", page.text)
    name_segments = name.groupdict()["name"].replace("_", " ").replace("-", " ").split()
    cls_name = "".join(map(lambda x: x.title(), name_segments))
    source_name = "_".join(map(lambda x: x.lower(), name_segments)) + ".py"
    source_path = f"./aocpy/solutions/{year}/{source_name}"
    inputs_path = f"inputs/{year}/{day}.txt"
    source = (
        "from aocpy.base import BaseSolution\n"
        "\n"
        "\n"
        f"class {cls_name}(BaseSolution, year={year}, day={day}):\n"
        f"    pass"
    )
    Path(source_path).write_text(source)
    print(f"Created source file: {source_path}")
    if settings.AOC_SESSION is None:
        print("Cannot get inputs, please set AOC_SESSION env.")
        return
    print("Trying to get inputs.")
    inputs = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        headers={"Cookie": f"session={settings.AOC_SESSION}"},
    )
    inputs.raise_for_status()

    Path(inputs_path).write_bytes(inputs.content)
    print(f"Created inputs: {inputs_path}")
    print(f"Task URL: https://adventofcode.com/{year}/day/{day}")


if __name__ == "__main__":
    cli()
