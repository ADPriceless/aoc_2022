def part1(trees):
    length = len(trees)
    width = len(trees[0])
    
    visible = [[0 for _ in row] for row in trees]
    scenic_scores = [[1 for _ in row] for row in trees]


    for y in range(length):
        for x in range(width):
            
            condition = x == 4 and y == 4

            # if condition:
            #     print(list(range(y - 1, -1, -1)))
            #     print(f'height = {trees[y][x]}')

            for north_y in range(y - 1, -1, -1):
                if trees[north_y][x] >= trees[y][x]:
                    scenic_scores[y][x] *= y - north_y
                    break
            else:
                scenic_scores[y][x] *= y
                visible[y][x] = 1

            for east_x in range(x + 1, width):
                if trees[y][east_x] >= trees[y][x]:
                    scenic_scores[y][x] *= east_x - x
                    break
            else:
                scenic_scores[y][x] *= width - 1 - x
                visible[y][x] = 1
            
            for south_y in range(y + 1, length):
                if trees[south_y][x] >= trees[y][x]:
                    scenic_scores[y][x] *= south_y - y
                    break
            else:
                scenic_scores[y][x] *= length - 1 - y
                visible[y][x] = 1

            for west_x in range(x - 1, -1, -1):
                if trees[y][west_x] >= trees[y][x]:
                    scenic_scores[y][x] *= x - west_x
                    break
            else:
                scenic_scores[y][x] *= x
                visible[y][x] = 1

    answer = sum(map(sum, visible))
    print(f'Part 1: {answer}')

    answer = max(map(max, scenic_scores))
    print(f'Part 2: {answer}')


def main():
    # with open('input\\day8.txt') as f:
    with open('input\\example8.txt') as f:
        lines = f.readlines()

    tree_heights = []
    for line in lines:
        trees = line.strip()
        tree_heights.append([int(tree) for tree in trees])

    part1(tree_heights)


if __name__ == '__main__':
    main()