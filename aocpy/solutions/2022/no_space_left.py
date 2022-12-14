from collections import deque
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from aocpy.base import BaseSolution


@dataclass
class TerminalCommand:
    command: str
    arguments: str
    output: list[str] = field(default_factory=list)


@dataclass
class FSNode:
    name: str
    path: Path
    is_file: bool
    size: Optional[int] = None
    parent: Optional["FSNode"] = None
    children: dict[str, "FSNode"] = field(default_factory=dict)


class NoSpaceLeftOnDevice(BaseSolution, year=2022, day=7):
    def parse_command_seq(self, inputs: list[str]) -> list[TerminalCommand]:
        commands = []
        for line in inputs:
            if line.startswith("$"):
                splitted = line.strip().split()
                commands.append(
                    TerminalCommand(
                        command=splitted[1],
                        arguments=" ".join(splitted[2:]),
                    )
                )
                continue
            commands[-1].output.append(line.strip())
        return commands

    def build_fs(self, commands: list[TerminalCommand]) -> FSNode:
        root_node = FSNode(name="/", path=Path("/"), is_file=False)
        current_node = root_node
        for command in commands:
            if command.command == "cd":
                if command.arguments == "/":
                    current_node = root_node
                elif command.arguments == "..":
                    current_node = current_node.parent
                else:
                    current_node = current_node.children[command.arguments]
            if command.command == "ls":
                for entry in command.output:
                    info, name = entry.split()
                    if info == "dir":
                        current_node.children[name] = FSNode(
                            name=name,
                            path=current_node.path / name,
                            is_file=False,
                            parent=current_node,
                        )
                    else:
                        current_node.children[name] = FSNode(
                            name=name,
                            path=current_node.path / name,
                            is_file=True,
                            size=int(info),
                            parent=current_node,
                        )
        self.find_sizes(root_node)
        return root_node

    @classmethod
    def find_sizes(cls, node: FSNode) -> int:
        if node.is_file:
            return node.size
        sum_size = 0
        for entry in node.children.values():
            sum_size += cls.find_sizes(entry)
        node.size = sum_size
        return node.size

    def fs_as_list(self, fs: FSNode) -> list[FSNode]:
        d = deque([fs])
        nodes = []
        while d:
            node = d.pop()
            nodes.append(node)
            for child in node.children.values():
                d.append(child)
        return nodes

    def part1(self, inputs: list[str]):
        commands = self.parse_command_seq(inputs)
        root = self.build_fs(commands)
        total = 0
        for node in self.fs_as_list(root):
            if not node.is_file and node.size < 100000:
                total += node.size
        return total

    def part2(self, inputs: list[str]):
        commands = self.parse_command_seq(inputs)
        root = self.build_fs(commands)
        fs_list = self.fs_as_list(root)
        fs_list.sort(key=lambda node: node.size)
        needed_space = 30000000 - (70000000 - root.size)
        for node in fs_list:
            if node.size >= needed_space:
                return node.size
        return "Has no solution, lol."
