from functools import cache


class Directory:
    def __init__(self, name: str, parent: str) -> None:
        self.name = name
        self.parent = parent
        self.children = []
        self.disk_usage = 0

    def add_to_disk_usage(self, file_size: str) -> None:
        self.disk_usage += int(file_size)

    @cache
    def sum_children(self):
        if len(self.children) == 0:
            return self.disk_usage
        else:
            for child in self.children:
                self.disk_usage += child.sum_children()
            return self.disk_usage

class FileSystem:
    def __init__(self, root: str) -> None:
        self.tree = {root: Directory('/', '/')}
        self.current_dir = root

    def process_line(self, line: str):
        parts = line.split(' ')
        self.parts = [part.strip() for part in parts]
        if self.parts[0] == '$':
            if self.parts[1] == 'cd':
                self.change_dir(self.parts[2])
            elif self.parts[1] == 'ls':
                pass # add contents to tree
        elif self.parts[0] == 'dir':
            self.add_dir(self.parts[1])
        elif self.parts[0].isnumeric():
            self.tree[self.current_dir].add_to_disk_usage(self.parts[0])
        else:
            raise ValueError(
                f'Unexpected argument in line {self.parts[0]}'
            )

    def change_dir(self, directory: str):
        if directory == '..':
            parent = self.tree[self.current_dir].parent
            self.current_dir = parent
        else:
            self.current_dir = directory

    def add_dir(self, name):
            dir_name = self.parts[1]
            current = self.tree[self.current_dir]
            if not dir_name in self.tree:
                new_dir = Directory(
                    name=name,
                    parent=self.current_dir
                )
                self.tree[dir_name] = new_dir
                current.children.append(new_dir)
                    

    def sum_directories_less_than(self, disk_usage_limit: int) -> int:
        total = 0
        self.tree['/'].sum_children()
        csdz = self.tree['csdz'].children
        print(f'csdz: {csdz}')
        for _, directory in self.tree.items():
            if directory.disk_usage <= disk_usage_limit:
                # print(f'{directory.parent}\\{directory.name}: {directory.disk_usage}')
                total += directory.disk_usage
        return total


def part1(input: list[str]) -> int:
    file_system = FileSystem(root='/')
    
    for line in input:
        file_system.process_line(line)
            
    answer = file_system.sum_directories_less_than(100_000)
    print(f'Part 1: {answer}')


def main():
    with open('input\\day7.txt') as f:
    # with open('input\\example7.txt') as f:
        lines = f.readlines()

    part1(lines) # 1119802


if __name__ == '__main__':
    main()
