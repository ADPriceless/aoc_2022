import aoc_utils

Coord_t = [int, int]
Cave_t = list[list[str]]


class Sand:
    def __init__(self, pos: Coord_t) -> None:
        self.pos = [pos[0], pos[1]]
        self.x_velocity = 0
        self.at_rest = False

    def check_below(self, cave: Cave_t, x_offset: int = 0) -> str:
        if self.pos[0] + 1 == len(cave):
            return 'void'
        try:
            return cave[self.pos[0] + 1][self.pos[1] + x_offset]
        except IndexError:
            print(f'y = {self.pos[0] + 1}, x = {self.pos[1] + x_offset}, x_offset = {x_offset}')

    def fall_down(self):
        if not self.at_rest:
            self.pos[0] += 1
            self.pos[1] += self.x_velocity

    def check_below_left(self, cave: Cave_t) -> str:
        return self.check_below(cave, x_offset=-1)

    def check_below_right(self, cave: Cave_t) -> str:
        return self.check_below(cave, x_offset=1)

    def rest(self, cave: Cave_t) -> None:
        self.at_rest = True
        y, x = self.pos[0], self.pos[1]
        cave[y][x] = 'O'


class FallingSandSimulator:
    def __init__(self, sand_start: Coord_t, cave: Cave_t, print_x_offset: int = 0) -> None:
        self.sand_start = sand_start
        self.cave = cave
        self.print_x_offset = print_x_offset
        self.num_sand_units = 0
        self.end_sim = False
        self.sand = None
        self._make_sand()
        self._tick_count = 0

    def run(self) -> int:
        while not self.end_sim:
            self._tick()
        return self.num_sand_units - 1

    def _tick(self):
        below_sand = self.sand.check_below(self.cave)
        if self.sand.at_rest:
            self._make_sand()
        elif below_sand == 'void':
            self.end_sim = True
        elif below_sand == '.': 
            self.sand.x_velocity = 0
        elif below_sand in ('O', '#'):
            if self.sand.check_below_left(self.cave) == '.':
                self.sand.x_velocity = -1
            elif self.sand.check_below_right(self.cave) == '.':
                self.sand.x_velocity = 1
            else:
                self.sand.x_velocity = 0
            if self.sand.x_velocity == 0:
                self.sand.rest(self.cave)
        self.sand.fall_down()


        # if self._tick_count < 300:
        #     print(f'Tick {self._tick_count}: n_sand = {self.num_sand_units}')
        #     print(f'Sand y, x = {self.sand.pos[0]}, {self.sand.pos[1]}')
        #     copy = [[ch for ch in row] for row in self.cave] # .copy() didn't work
        #     try:
        #         copy[self.sand.pos[0]][self.sand.pos[1]] = '+'
        #         print_cave(copy, self.print_x_offset - 1)
        #     except IndexError:
        #         pass            
        #     self._tick_count += 1
        # else:
        #     self.end_sim = True

    def _make_sand(self): # Anakin raging
        self.sand = Sand(self.sand_start)
        self.num_sand_units += 1


class CaveGenerator:
    def __init__(self, aoc_input: list[str]) -> None:
        self.aoc_input = aoc_input
        self.coords = []
        self.y_min, self.y_max, self.x_min, self.x_max = 0, 0, 0, 0

    def make_cave_system(self) -> Cave_t:
        self._parse_input_for_coords()
        self._get_min_max()
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
        
    def get_x_min(self):
        return self.x_min

    def _create_canvas(self) -> None:
        self.canvas = [['.' for _ in range(self.x_max + 1)] \
            for _ in range(self.y_max + 1)]

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


def print_cave(cave: Cave_t, x_offset: int = 0):
    for row in cave:
        print(''.join(row[x_offset:]))

def main():
    print('----- Start -----')
    # aoc_input = aoc_utils.readlines('input\\example14.txt')
    aoc_input = aoc_utils.readlines('input\\day14.txt')
    cave_gen = CaveGenerator(aoc_input)
    cave_system = cave_gen.make_cave_system()
    # sand_start = cave_gen.get_sand_start()
    x_offset = cave_gen.get_x_min()
    sim = FallingSandSimulator((0, 500), cave_system, print_x_offset=x_offset)
    answer = sim.run()
    print(f'Part 1: {answer}')

if __name__ == '__main__':
    main()
