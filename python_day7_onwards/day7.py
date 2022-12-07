class Directory:
    ...


class Directory:
    def __init__(self, name: str, parent: Directory | None) -> None:
        self.name = name
        self.parent = parent
        self.children = []
        self.disk_usage = 0

    def add_to_disk_usage(self, file_size: str) -> None:
        self.disk_usage += int(file_size)

    def sum_children(self):
        if len(self.children) == 0:
            return self.disk_usage
        else:
            for child in self.children:
                self.disk_usage += child.sum_children()
            return self.disk_usage

    def sum_less_than(self, value):
        total = 0
        for child in self.children:
            total += child.sum_less_than(value)

        if self.disk_usage < value:
            return self.disk_usage + total
        else:
            return total
                

class FileSystem:
    def __init__(self) -> None:
        self.root = Directory('/', None)
        self.current_dir = self.root

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
            self.current_dir.add_to_disk_usage(self.parts[0])
        else:
            raise ValueError(
                f'Unexpected argument in line {self.parts[0]}!'
            )

    def change_dir(self, new_directory: str):
        previous = self.current_dir
        if new_directory == '..':
            parent = self.current_dir.parent
            if parent is not None:
                self.current_dir = parent
        elif new_directory == '/':
            self.current_dir = self.root
        else:
            for child in self.current_dir.children:
                if child.name == new_directory:
                    self.current_dir = child
                    break
            else:
                raise ValueError(f"Could not find '{new_directory}' in '{self.current_dir.name}'!")
        print(f"cd '{previous.name}' to '{self.current_dir.name}'")

    def add_dir(self, name):
        print(f"Add '{name}' to '{self.current_dir.name}'")
        new_dir = Directory(
            name=name,
            parent=self.current_dir
        )
        self.current_dir.children.append(new_dir)
                    
    def sum_directories_less_than(self, disk_usage_limit: int) -> int:
        self.root.sum_children()
        return self.root.sum_less_than(disk_usage_limit)


def part1(input: list[str]) -> int:
    file_system = FileSystem()
    
    for line in input:
        file_system.process_line(line)
            
    answer = file_system.sum_directories_less_than(100_000)
    print(f'Part 1: {answer}')


def main():
    with open('input\\day7.txt') as f:
    # with open('input\\example7.txt') as f:
        lines = f.readlines()

    part1(lines) 


if __name__ == '__main__':
    main()
