from collections import defaultdict
from dataclasses import dataclass, field
from typing import DefaultDict

from aocpy.base import BaseSolution
from aocpy.utils.vec2 import Vec2


@dataclass
class Graph:
    vertices: list[Vec2]
    edges: DefaultDict[Vec2, list[Vec2]] = field(
        default_factory=lambda: defaultdict(list),
    )

    def get_distances(self, src: Vec2) -> dict[Vec2, float]:
        dist = {}
        prev = {}
        nodes_queue: list[Vec2] = []

        for vertice in self.vertices:
            dist[vertice] = float("inf")
            prev[vertice] = None
            nodes_queue.append(vertice)

        dist[src] = 0

        while nodes_queue:
            nodes_queue.sort(key=lambda v: dist[v])
            node = nodes_queue.pop(0)

            for neighbour in self.edges[node]:
                alt = dist[node] + 1
                if alt < dist[neighbour]:
                    dist[neighbour] = alt
                    prev[neighbour] = node

        return dist


@dataclass
class Board:
    your_position: Vec2
    destination: Vec2
    graph: Graph
    location_map: list[list[int]]


# This is an awful solution. Please don't beat me.
class HillClimbingAlgorithm(BaseSolution, year=2022, day=12):
    def construct_board(
        self,
        inputs: list[str],
        reversed: bool = False,
    ) -> Board:
        location_map = []
        your_position = Vec2(0, 0)
        destination = Vec2(0, 0)
        for y, line in enumerate(inputs):
            location_map.append([])
            for x, char in enumerate(line.strip()):
                if char == "S":
                    your_position = Vec2(x=x, y=y)
                    char = "a"
                if char == "E":
                    destination = Vec2(x=x, y=y)
                    char = "z"
                location_map[-1].append(ord(char) - 97)

        graph = Graph(vertices=[], edges=defaultdict(list))

        for y in range(len(location_map)):
            for x in range(len(location_map[y])):
                vertex = Vec2(x=x, y=y)
                graph.vertices.append(vertex)
                for delta in {Vec2(1, 0), Vec2(0, 1), Vec2(-1, 0), Vec2(0, -1)}:
                    new_edge = vertex + delta
                    if new_edge.x < 0 or new_edge.x >= len(location_map[y]):
                        continue
                    if new_edge.y < 0 or new_edge.y >= len(location_map):
                        continue

                    delta = (
                        location_map[new_edge.y][new_edge.x]
                        - location_map[vertex.y][vertex.x]
                    )

                    if reversed:
                        delta = (
                            location_map[vertex.y][vertex.x]
                            - location_map[new_edge.y][new_edge.x]
                        )

                    if delta > 1:
                        continue

                    graph.edges[vertex].append(new_edge)

        return Board(
            your_position=your_position,
            destination=destination,
            location_map=location_map,
            graph=graph,
        )

    def part1(self, inputs: list[str]):
        board = self.construct_board(inputs)
        return board.graph.get_distances(
            board.your_position,
        )[board.destination]

    def part2(self, inputs: list[str]):
        board = self.construct_board(inputs, reversed=True)
        distances = board.graph.get_distances(board.destination)
        min_dist = float("inf")
        for y in range(len(board.location_map)):
            for x in range(len(board.location_map[y])):
                if board.location_map[y][x] == 0:
                    dist = distances[Vec2(x=x, y=y)]
                    if dist < min_dist:
                        min_dist = dist

        return min_dist
