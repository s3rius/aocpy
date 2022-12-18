from aocpy.base import BaseSolution
from dataclasses import dataclass, field


@dataclass
class Pipe:
    id: str
    flow_rate: int
    tunnels: dict[str, "Pipe"] = field(default_factory=dict)


class ProboscideaVolcanium(BaseSolution, year=2022, day=16):
    def build_pipes(self, inputs: list[str]) -> dict[str, Pipe]:
        pipes: "dict[str, Pipe]" = {}
        tunnels = {}
        for line in inputs:
            parsed = line.strip().split(";")
            pipe_id = parsed[0].split()[1]
            rate = int(parsed[0].split("rate=")[1])
            paths = list(map(lambda x: x.strip(","), parsed[1].split()[4:]))
            tunnels[pipe_id] = paths
            pipes[pipe_id] = Pipe(
                id=pipe_id,
                flow_rate=rate,
            )
        for pipe in pipes.values():
            pipe_tunnels = {}
            for tun in tunnels[pipe.id]:
                pipe_tunnels[tun] = pipes[tun]
            pipe.tunnels = pipe_tunnels

        return pipes
