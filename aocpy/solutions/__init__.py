import pkgutil
from importlib import import_module
from pathlib import Path


def load_all_solutions() -> None:
    package_dir = Path(__file__).resolve().parent
    for dir in package_dir.iterdir():
        modules = pkgutil.walk_packages(
            path=[str(dir)],
            prefix=f"aocpy.solutions.{dir.name}.",
        )
        for module in modules:
            import_module(module.name)  # noqa: WPS421
