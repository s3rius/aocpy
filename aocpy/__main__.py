import inspect
import sys
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser, Namespace
from pathlib import Path

from typer import Typer

from aocpy.base import BaseSolution
from aocpy.solutions import load_all_solutions

cli = Typer()


def parse_args() -> Namespace:
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("year", type=int, help="Which year to solve.")
    parser.add_argument("day", type=int, help="Which day to solve.")
    parser.add_argument("--test", action="store_true", help="Run over test values.")
    return parser.parse_args()


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


if __name__ == "__main__":
    cli()
