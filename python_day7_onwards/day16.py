import aoc_utils


class Vertex:
    def __init__(self, name: str, flow_rate: int, adjacent: list[str]) -> None:
        self.name = name
        self.flow_rate = flow_rate
        self.adjacent = tuple(adjacent) # this must not be changed
        self.distance = dict(zip(adjacent, [1 for _ in adjacent]))
        # print(f'name: {name}, adjacent: {self.distance}')

    def __repr__(self) -> str:
        return f'Vertex {self.name}: flow rate = {self.flow_rate}'


def create_vertices(aoc_input: list[str]) -> list[Vertex]:
    vertices = []
    for line in aoc_input:
        parts = line.split(' ')
        name = parts[1]
        flow_rate = int(parts[4][5:-1])
        if ',' in line:
            adjacent = line[line.index('valves ') + len('valves '):].split(', ')
        else:
            adjacent = [line[line.index('valve ') + len('valve '):]]
        vertices.append(Vertex(name, flow_rate, adjacent))
    return vertices


class Graph:
    def __init__(self, vertices: list[Vertex]) -> None:
        self.vertices = dict(zip([v.name for v in vertices], vertices))
        # MAX can be len(vertices) bc distance between each is 1 so longest path is n-1
        self.num_vertices = self.MAX = len(vertices)

    def dijkstra(self, source: str):
        self.shortest_path_tree = set(source)
        distance = dict(
            zip([v.name for v in self.vertices.values()], [self.MAX for _ in self.vertices])
        )
        distance[source] = 0

        for _ in range(self.num_vertices):
            closest = self.closest_to_source(distance)
            self.shortest_path_tree.add(closest.name)

            for adjacent in closest.adjacent:
                if adjacent not in self.shortest_path_tree \
                    and distance[adjacent] > distance[closest.name] + closest.distance[adjacent]:
                    distance[adjacent] = distance[closest.name] + closest.distance[adjacent]
        
        return distance

    def closest_to_source(self, distance: dict) -> Vertex:
        min_dist = self.MAX
        min_name = ''
        for name, dist in distance.items():
            if dist < min_dist and name not in self.shortest_path_tree:
                min_dist = dist
                min_name = name
        return self.vertices[min_name]


def print_shortest_paths(shortest_paths: list[dict]):
    keys = shortest_paths[0].keys()
    columns = ' '.join(keys)
    print(f'  |{columns}')
    print(f'-' * (len(columns) + 3))
    for key, path in zip(keys, shortest_paths):
        values = [str(v) for v in path.values()]
        values = '  '.join(values)
        print(f'{key}| {values}')



def main():
    aoc_input = aoc_utils.readlines(
        'input\\example16.txt', remove_trailing_newline=True
    )
    shortest_paths = []
    vertices = create_vertices(aoc_input)
    graph = Graph(vertices)
    for vertex in vertices:
        shortest_paths.append(graph.dijkstra(vertex.name))
    print_shortest_paths(shortest_paths)


if __name__ == '__main__':
    main()
