import aoc_utils
import colorama


def calc_route(parent: dict, goal_pos):
    route = []
    pos = parent[goal_pos]
    while pos is not None:
        route.append(pos)
        pos = parent[pos]
    return route
        

def bredth_first(game_input):
    h_map = [[ord(n) for n in line.strip()] for line in game_input]
    goal = 'E'
    player = 'S'
    for y, row in enumerate(game_input):
        if 'S' in row:
            x = row.index(player)
            start_pos = (y, x)
            h_map[y][x] = ord('a') # start at height a
        if goal in row:
            x = row.index(goal)
            goal_pos = (y, x)
            h_map[y][x] = ord('z') # goal is at height z
    explored = [start_pos]
    queue_ = [start_pos]
    parent = {start_pos: None}

    while len(queue_) > 0:
        pos = queue_.pop(0)
        if pos == goal_pos:
            route = calc_route(parent, goal_pos)
            print_result(game_input, route, pos)
            return len(route)
        for edge in adjacent(pos, h_map):
            if edge not in explored:
                if reachable(pos, edge, h_map):
                    explored.append(edge)
                    queue_.append(edge)
                    parent[edge] = pos
    raise RuntimeError("Couldn't find a solution :(")


def adjacent(pos, h_map) -> list[list[int, int]]:
    adjacent = []
    if pos[0] - 1 >= 0:
        adjacent.append((pos[0] - 1, pos[1]))
    if pos[0] + 1 < len(h_map):
        adjacent.append((pos[0] + 1, pos[1]))
    if pos[1] - 1 >= 0:
        adjacent.append((pos[0], pos[1] - 1))
    if pos[1] + 1 < len(h_map[0]):
        adjacent.append((pos[0], pos[1] + 1))
    return adjacent


def reachable(pos, adjacent, h_map) -> bool:
    if h_map[adjacent[0]][adjacent[1]] - h_map[pos[0]][pos[1]] <= 1:
        return True
    else:
        return False


def print_result(game_input, route, last):
    special = ('S', 'E')
    for y, row in enumerate(game_input):
        for x, char in enumerate(row.rstrip()):
            if char > 'u':
                back = colorama.Back.WHITE
            elif char > 'q':
                back = colorama.Back.LIGHTCYAN_EX
            elif char > 'm':
                back = colorama.Back.LIGHTBLUE_EX
            elif char > 'i':
                back = colorama.Back.CYAN 
            elif char > 'e':
                back = colorama.Back.BLUE
            elif char == 'b':
                back = colorama.Back.YELLOW
            else:
                back = colorama.Back.BLACK
            if all(((y, x) in route, char not in special, (y, x) != last)):
                print(f'{colorama.Fore.RESET}{colorama.Back.GREEN}{char}', end='')
            elif char in special:
                print(f'{colorama.Fore.RED}{back}{char}', end='')
            else:
                print(f'{colorama.Fore.RESET}{back}{char}', end='')
        print(colorama.Back.RESET + colorama.Fore.RESET)


def main():
    colorama.init()
    # lines = aoc_utils.readlines('.\\input\\example12.txt')
    lines = aoc_utils.readlines('.\\input\\day12.txt')
    answer = bredth_first(lines)
    print(f'Part 1: {answer}')
    # part 2 solved visually


if __name__ == '__main__':
    main()
