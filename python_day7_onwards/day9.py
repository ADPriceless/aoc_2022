import aoc_utils


class Rope:
    def __init__(self, x, y) -> None:
        self.x, self.y = x, y
        self.prev_x, self.prev_y = x, y
        self.visited = []

    def move(self, direction: str) -> None:
        self.prev_x, self.prev_y = self.x, self.y
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

    def distance_to(self, rope) -> int:
        return (self.x - rope.x)**2 + (self.y - rope.y)**2

    def follow(self, rope):
        self.x, self.y = rope.prev_x, rope.prev_y

    def add_to_visited(self) -> None:
        coord = (self.x, self.y)
        if coord not in self.visited:
            self.visited.append(coord)


def print_area(head: Rope, tail: Rope):
    """Only good for small areas e.g. example input"""
    n = 7
    area = [['.' for _ in range(n)] for _ in range(n)]
    area[head.y][head.x] = 'H' # swap x and y bc lists are row-major
    area[tail.y][tail.x] = 'T'
    area.reverse() # reverse bc increasing y moves down rows
    for row in area:
        for thing in row:
            print(thing, end='')
        print()
    print()


def part1(lines: list[str]) -> int: 
    head = Rope(0, 0)
    tail = Rope(0, 0)
    tail.add_to_visited() # add initial spot [0, 0]

    for line in lines:
        motion = line.split(' ')
        direction, distance = motion[0], int(motion[1])

        for _ in range(distance):
            head.move(direction)
            if tail.distance_to(head) >= 4:
                tail.follow(head)
                tail.add_to_visited()
            # print_area(head, tail)

    num_visited = len(tail.visited)
    print(f'Part 1: {num_visited}')


def main():
    # lines = aoc_utils.readlines('input\\example9.txt')
    lines = aoc_utils.readlines('input\\day9.txt')
    part1(lines)


if __name__ == '__main__':
    main()