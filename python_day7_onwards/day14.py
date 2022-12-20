import aoc_utils

Coord_t = [int, int]
Cave_t = list[list[str]]


class Sand:
    pass


class FallingSandSimulator:
    def __init__(self, sand_start: Coord_t, cave: Cave_t) -> None:
        self.sand_start = sand_start
        self.cave = cave
        self.num_sand_units = 0
        self.end_sim = False

    def run(self):
        while not self.end_sim:
            self._tick()

    def _tick(self):
        # if air below sand:
            # move sand down one unit
        # else:
            # check if rock below and land
            # check if sand below and decide where to land
            # check if fallen off the edge (end simulation)
        pass


class CaveGenerator:
    PADDING: int = 1

    def __init__(self, aoc_input: list[str]) -> None:
        self.aoc_input = aoc_input
        self.coords = []
        self.y_min, self.y_max, self.x_min, self.x_max = 0, 0, 0, 0

    def make_cave_system(self) -> Cave_t:
        self._parse_input_for_coords()
        self._get_min_max()
        self._rebias_coords()
        self._create_canvas()
        self._draw_lines_to_canvas()
        return self.canvas

    def _parse_input_for_coords(self) -> None:
        for line in self.aoc_input:
            connected_coords = line.split(' -> ')
            line_coords = [[int(coord.split(',')[0]), int(coord.split(',')[1])] for coord in connected_coords]
            self.coords.append(line_coords)

    def _get_min_max(self):
        self.x_min = min([min([coord[0] for coord in line]) for line in self.coords])
        self.x_max = max([max([coord[0] for coord in line]) for line in self.coords])
        self.y_min = min([min([coord[1] for coord in line]) for line in self.coords])
        self.y_max = max([max([coord[1] for coord in line]) for line in self.coords])
        
    def _rebias_coords(self) -> None:
        """Set coords to start indented by the padding"""
        for line in self.coords:
            for coord in line:
                coord[0] -= self.x_min - self.PADDING
                coord[1] -= self.y_min - self.PADDING

    def _create_canvas(self) -> None:
        self.canvas = [['.' for _ in range(self.x_min, self.x_max + 1 + 2*self.PADDING)] \
            for _ in range(self.y_min, self.y_max + 1 + 2*self.PADDING)]

    def _draw_lines_to_canvas(self) -> None:
        for coords in self.coords:
            for i in range(1, len(coords)):
                self._draw_line(coords[i-1], coords[i])

    def _draw_line(self, start: Coord_t, stop: Coord_t) -> None:
        x_step = 1 if start[0] < stop[0] else -1
        y_step = 1 if start[1] < stop[1] else -1
        for y in range(start[1], stop[1] + y_step, y_step):
            for x in range(start[0], stop[0] + x_step, x_step):
                self.canvas[y][x] = '#'


def main():
    aoc_input = aoc_utils.readlines('input\\example14.txt')
    cave_gen = CaveGenerator(aoc_input)
    cave_system = cave_gen.make_cave_system()
    for row in cave_system:
        print(''.join(row))

if __name__ == '__main__':
    main()
