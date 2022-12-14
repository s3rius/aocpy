from aocpy.base import BaseSolution


class TheTreacheryOfWhales(BaseSolution, year=2021, day=7):
    def part1(self, inputs: list[str]):
        points = list(map(int, inputs[0].strip().split(",")))
        min_fuel_cost = float("inf")
        for point in points:
            fuel_cons = sum(map(lambda x: abs(point - x), points))
            if fuel_cons < min_fuel_cost:
                min_fuel_cost = fuel_cons
        return min_fuel_cost

    def part2(self, inputs: list[str]):
        points = list(map(int, inputs[0].strip().split(",")))
        min_fuel_cost = float("inf")
        for point in range(min(points), max(points) + 1):
            fuel_cons = sum(map(lambda x: sum(range(abs(point - x) + 1)), points))
            if fuel_cons < min_fuel_cost:
                min_fuel_cost = fuel_cons
        return min_fuel_cost
