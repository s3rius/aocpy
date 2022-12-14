import math
from collections import deque
from dataclasses import dataclass
from typing import Callable

from aocpy.base import BaseSolution


@dataclass
class Monkey:
    id: int
    items: deque[int]
    operation: Callable[[int], int]
    test_val: int
    success_test_mnk: int
    failed_test_mnk: int
    inspected_items: int = 0


class MonkeyInTheMiddle(BaseSolution, year=2022, day=11):
    def parse_one_monkey(self, monkey_spec: list[str]) -> Monkey:
        monkey_id = -1
        items = []
        operation = lambda x: x
        test_val = -1
        success_mnk = -1
        fail_mnk = -1
        for line in monkey_spec:
            if line.strip().startswith("Monkey"):
                monkey_id = int(line.strip().removeprefix("Monkey ").removesuffix(":"))
            if line.strip().startswith("Starting"):
                items = list(
                    map(
                        int,
                        map(
                            lambda x: x.strip(),
                            line.strip().split(":")[1].split(","),
                        ),
                    ),
                )
            elif line.strip().startswith("Operation"):
                _, operation_text = line.strip().split("=")
                func_text = f"lambda old: {operation_text}"
                operation = eval(func_text)
            elif line.strip().startswith("Test"):
                _, val = line.strip().split("divisible by")
                test_val = int(val)
            elif line.strip().startswith("If true"):
                _, val = line.strip().split("throw to monkey")
                success_mnk = int(val)
            elif line.strip().startswith("If false"):
                _, val = line.strip().split("throw to monkey")
                fail_mnk = int(val)

        return Monkey(
            id=monkey_id,
            items=deque(items),
            operation=operation,
            test_val=test_val,
            success_test_mnk=success_mnk,
            failed_test_mnk=fail_mnk,
        )

    def parse_monkeys(self, inputs: list[str]) -> list[Monkey]:
        monkeys = []
        buffer = []
        for line_idx, line in enumerate(inputs):
            buffer.append(line)
            if line.strip() == "" or line_idx == len(inputs) - 1:
                monkeys.append(self.parse_one_monkey(buffer))
                buffer = []
                continue
        return monkeys

    def simulate(self, monkeys: list[Monkey], rounds: int, use_lcm: bool) -> int:
        monkeys = sorted(monkeys, key=lambda mnk: mnk.id)
        lcm = math.lcm(*list(map(lambda m: m.test_val, monkeys)))
        for _ in range(rounds):
            for mnk in monkeys:
                while mnk.items:
                    item = mnk.items.popleft()
                    if use_lcm:
                        new_level = mnk.operation(item) % lcm
                    else:
                        new_level = mnk.operation(item) // 3
                    mnk.inspected_items += 1
                    if new_level % mnk.test_val == 0:
                        monkeys[mnk.success_test_mnk].items.append(new_level)
                    else:
                        monkeys[mnk.failed_test_mnk].items.append(new_level)
        ins1, ins2 = sorted(
            map(lambda mnk: mnk.inspected_items, monkeys),
            reverse=True,
        )[:2]
        return ins1 * ins2

    def part1(self, inputs: list[str]):
        monkeys = self.parse_monkeys(inputs)
        return self.simulate(monkeys, 20, False)

    def part2(self, inputs: list[str]):
        monkeys = self.parse_monkeys(inputs)
        return self.simulate(monkeys, 10000, True)
