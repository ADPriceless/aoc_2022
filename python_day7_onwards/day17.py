import logging

import aoc_utils


ROCKS = (
    ('####',),

    ('.#.', 
     '###',
     '.#.'),

    ('..#',
     '..#',
     '###'),

    ('#',
     '#',
     '#',
     '#'),

    ('##',
     '##'),
)


def calc_initial_y() -> int:
    return 3


def print_game(rock, x, y, w: int) -> None:
    rock_height = len(rock)
    rock_width = len(rock[0])
    print()
    print()
    for row in range(rock_height + y):
        if row < rock_height:
            to_print = '|' + '.' * x + rock[row] + '.' * (w - rock_width - x) + '|'
        else:
            to_print = '|' + '.' * w + '|'
        print(to_print)
    print('+-------+')


def part1():
    WIDTH = 7

    input = aoc_utils.readlines("input\\example17.txt")[0]
    floor_level = [0 for _ in range(WIDTH)]

    x = 2 
    y = calc_initial_y()

    current_rock = 0
    rock = ROCKS[current_rock]
    rock_w = len(rock[0])

    logging.info('x=%d, y=%d', x, y)

    for direction in input:
        if direction == '<':
            if x > 0:
                x -= 1
        elif direction == '>':
            if x + rock_w < WIDTH:
                x += 1
        else:
            raise ValueError(f'Direction ({direction}) must be < or >')
        
        y -= 1

        logging.info('x=%d, y=%d', x, y)
        print_game(rock, x, y, WIDTH)

        if y == floor_level[x]:
            x = 2
            y = calc_initial_y()
            current_rock = (current_rock + 1) % len(ROCKS)
            rock = ROCKS[current_rock]
            rock_w = len(rock[0])
            print('Hit the bottom!')


def main():
    logging.basicConfig(filename='aoc.log', filemode='w', level=logging.INFO)
    part1()


main()
