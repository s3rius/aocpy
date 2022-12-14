from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, Namespace
from aocpy.solutions import load_all_solutions
from aocpy.base import BaseSolution
import inspect
from pathlib import Path
import sys


def parse_args() -> Namespace:
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("year", type=int, help="Which year to solve.")
    parser.add_argument("day", type=int, help="Which day to solve.")
    parser.add_argument("--test", action="store_true", help="Run over test values.")
    return parser.parse_args()


def main():
    args = parse_args()
    load_all_solutions()
    try:
        solution = BaseSolution.solutions[(args.year, args.day)]
    except LookupError:
        print(f"Solution for {args.year}:{args.day} cannot be found.")
        return 1

    solution_path = Path(inspect.getfile(solution.__class__)).relative_to(
        Path(__file__).parent,
    )
    print(f"Running solution from file: {solution_path}")
    solution.run(args.test)


if __name__ == "__main__":
    sys.exit(main() or 0)
