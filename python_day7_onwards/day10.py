import aoc_utils


class Processor:
    def __init__(self) -> None:
        self.register_x = 1
        self.cycles = 0
        self.signal_strength_total = 0
        self.reset_pixels()
        self.draw_on_screen()

    def noop(self):
        self.cycles += 1
        self.check_cycles()
        self.draw_on_screen()

    def addx(self, value):
        self.cycles += 1
        self.check_cycles()
        self.draw_on_screen()
        self.cycles += 1
        self.check_cycles()
        self.register_x += value # updated at end of 2nd cycle
        self.draw_on_screen()

    def check_cycles(self):
        if self.cycles == 20:
            self.sum_signal_strength()
        elif (self.cycles - 20) % 40 == 0 and self.cycles <= 220:
            self.sum_signal_strength()

    def sum_signal_strength(self):
        self.signal_strength_total += \
            self.register_x * self.cycles

    def draw_on_screen(self):
        pix = self.cycles % 40
        if  pix == 0:
            print(''.join(self.pixels))
            self.reset_pixels()
    
        if (pix == self.register_x - 1) and (self.register_x - 1 >= 0):
            self.pixels[pix] = '#'
        elif pix == self.register_x:
            self.pixels[pix] = '#'
        elif (pix == self.register_x + 1) and (self.register_x + 1 < 40):
            self.pixels[pix] = '#'
        
        # if self.cycles < 10:
        #     print(f'cycle {self.cycles}: pix = {pix}, x = {self.register_x}, pixel = {self.pixels[pix]}')

    def reset_pixels(self):
        self.pixels = ['.' for _ in range(40)]


def part1(input: list[str]) -> None:
    processor = Processor()

    for instruction in input:
        instruction_parts = aoc_utils.split_and_cast(instruction)
        if instruction_parts[0] == 'noop':
            processor.noop()
        elif instruction_parts[0] == 'addx':
            processor.addx(instruction_parts[1])
        else:
            raise ValueError(f'Unknown instruction: {instruction}')

    print(f'Part 1: {processor.signal_strength_total}')


def part2(input: list[str]) -> None:
    processor = Processor()

    for instruction in input:
        instruction_parts = aoc_utils.split_and_cast(instruction)
        if instruction_parts[0] == 'noop':
            processor.noop()
        elif instruction_parts[0] == 'addx':
            processor.addx(instruction_parts[1])
        else:
            raise ValueError(f'Unknown instruction: {instruction}')


def main():
    # lines = aoc_utils.readlines('input\\example10.txt')
    lines = aoc_utils.readlines('input\\day10.txt')
    part1(lines)

if __name__ == '__main__':
    main()