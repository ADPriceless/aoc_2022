import aoc_utils


class Knot:
    def __init__(self, x, y, next_knot=None, idx=0) -> None:
        self.x, self.y = x, y
        self.prev_x, self.prev_y = x, y
        self.visited = []
        self.next = next_knot
        self.idx = idx

    def move(self, direction: str) -> None:
        if direction == 'U':
            self.y += 1
        elif direction == 'R':
            self.x += 1
        elif direction == 'D':
            self.y -= 1
        elif direction == 'L':
            self.x -= 1
        else:
            raise ValueError('Not a valid direction!')

    def distance_to(self, knot) -> int:
        return (self.x - knot.x)**2 + (self.y - knot.y)**2

    def distance_to_next(self):
        if not self.next:
            return 0
        else:
            return (self.distance_to(self.next))

    def follow(self, knot):
        if self.x < knot.x:
            self.x += 1
        elif self.x > knot.x:
            self.x -= 1
        if self.y < knot.y:
            self.y += 1
        elif self.y > knot.y:
            self.y -= 1

    def add_to_visited(self) -> None:
        coord = (self.x, self.y)
        if coord not in self.visited:
            self.visited.append(coord)


def print_area(rope, n=7):
    """Only good for small areas e.g. example input"""
    area = [['.' for _ in range(n)] for _ in range(n)]
    for knot in rope:
        area[knot.y][knot.x] = str(knot.idx)
    area.reverse() # reverse bc increasing y moves down rows
    for row in area:
        for thing in row:
            print(thing, end='')
        print()
    print()


def part1(lines: list[str]) -> int:
    head = Knot(0, 0)
    tail = Knot(0, 0)
    tail.add_to_visited() # add initial spot [0, 0]

    for line in lines:
        motion = line.split(' ')
        direction, distance = motion[0], int(motion[1])

        for _ in range(distance):
            head.move(direction)
            if tail.distance_to(head) >= 4:
                tail.follow(head)
                tail.add_to_visited()
            # print_area([head, tail])

    num_visited = len(tail.visited)
    print(f'Part 1: {num_visited}')


def part2(lines: list[str]) -> int:
    rope = [Knot(0, 0, idx=i) for i in range(10)]
    for i in range(1, 10):
        rope[i].next = rope[i-1]

    head = rope[0]
    tail = rope[-1]
    tail.add_to_visited() # add initial spot [0, 0]

    for line in lines:
        motion = line.split(' ')
        direction, distance = motion[0], int(motion[1])

        for _ in range(distance):
            head.move(direction)
            for knot in rope:
                if knot.distance_to_next() >= 4:
                    knot.follow(knot.next)
                    knot.add_to_visited()
            # print_area(rope, n=7)

    num_visited = len(tail.visited)
    print(f'Part 2: {num_visited}')


def main():
    # lines = aoc_utils.readlines('input\\example9.txt')
    lines = aoc_utils.readlines('input\\day9.txt')
    part1(lines)
    part2(lines)


if __name__ == '__main__':
    main()
