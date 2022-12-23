import aoc_utils


class Vertex:
    def __init__(self, name: str, connections: list[str], flow_rate: int) -> None:
        self.name = name
        self.connections = connections
        self.flow_rate = flow_rate
        self.spt_set = set()
        self.distance = {}


def create_vertices(aoc_input: list[str]) -> list[Vertex]:
    vertices = []
    for line in aoc_input:
        parts = line.split(' ')
        name = parts[1]
        flow_rate = int(parts[4][5:-2])
        connections = None



def main():
    pass


if __name__ == '__main__':
    main()
