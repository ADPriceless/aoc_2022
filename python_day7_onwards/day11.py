import math

import aoc_utils


class Jungle:

    NUMBER_OF_ROUNDS = 20

    def __init__(self, notes: list[str]) -> None:
        self.notes = notes
        self.monkeys = []

    def make_monkeys(self):
        for line in self.notes:
            note = line.strip()
            if note.startswith('Monkey'):
                monkey_id = int(note.split(' ')[1][0]) # get n from line: "Monkey n:"
                monkey = Monkey(monkey_id)
                self.monkeys.append(monkey)
            elif note.startswith('Starting'):
                monkey.steal_starting_items(note)
            elif note.startswith('Operation'):
                monkey.set_operation(note)
            elif note.startswith('Test'):
                monkey.set_test_operand(note)
            elif note.startswith('If true'):
                monkey.set_pass_monkey(note)
            elif note.startswith('If false'):
                monkey.set_fail_monkey(note)
        
    def monkey_around(self):
        for _ in range(self.NUMBER_OF_ROUNDS):
            for monkey in self.monkeys:
                monkey.print_id()
                # print(f'Items {monkey.items}')
                for item in monkey.items:
                    monkey.inspect(item)
                    monkey.do_operation()
                    monkey.get_bored()
                    receive_monkey_id, item = monkey.test_and_throw_item()
                    self.monkeys[receive_monkey_id].catch(item)
                monkey.done_throwing()

    def calculate_monkey_business(self):
        num_inspects = [monkey.num_inspects for monkey in self.monkeys]
        num_inspects.sort(reverse=True)
        # print(f'num_inspects = {num_inspects}')
        return num_inspects[0] * num_inspects[1]


class Monkey:
    def __init__(self, id_: int, print_actions=False) -> None:
        self.id = id_
        self.items = []
        self.worry_level = 0
        self.worry_operand = 0
        self.test_operand = 0
        self.pass_monkey = 0
        self.fail_monkey = 0
        self.num_inspects = 0
        self.print_actions = print_actions

    def print_id(self):
        if self.print_actions:
            print(f'Monkey {self.id}:')

    def steal_starting_items(self, starting_items_note: str):
        items_idx = starting_items_note.find(':') + 1
        starting_items = starting_items_note[items_idx:]
        items = starting_items.split(', ')
        for item in items:
            self.items.append(int(item.strip()))

    def set_operation(self, operation: str):
        idx = operation.find('old ')
        parts = operation[idx+4:].split(' ')
        if parts[0] == '*':
            self.operation = self._multiply
        elif parts[0] == '+':
            self.operation = self._add
        elif parts[0] == '-':
            self.operation = self._subtract
        elif parts[0] == '/':
            self.operation = self._divide
        else:
            raise ValueError(f'Invalid operation: {parts[0]}')
        if parts[1] == 'old':
            self.worry_operand = 'old'
        else:
            self.worry_operand = int(parts[1].rstrip())

    def _multiply(self):
        if self.worry_operand == 'old':
            self.worry_level *= self.worry_level
        else:
            self.worry_level *= self.worry_operand
        if self.print_actions:
            print(f'\t\tWorry level is multiplied by {self.worry_operand} to {self.worry_level}.')
    
    def _add(self):
        if self.worry_operand == 'old':
            self.worry_level += self.worry_level
        else:
            self.worry_level += self.worry_operand
        if self.print_actions:
            print(f'\t\tWorry level increases by {self.worry_operand} to {self.worry_level}.')

    def _subtract(self):
        if self.worry_operand == 'old':
            self.worry_level -= self.worry_level
        else:
            self.worry_level -= self.worry_operand
        if self.print_actions:
            print(f'\t\tWorry level decreases by {self.worry_operand} to {self.worry_level}.')

    def _divide(self):
        if self.worry_operand == 'old':
            self.worry_level = 1
        else:
            self.worry_level = self.worry_level // self.worry_operand
        if self.print_actions:
            print(f'\t\tWorry level is divided by {self.worry_operand} to {self.worry_level}.')

    def set_test_operand(self, test: str):
        parts = test.split(' ')
        self.test_operand = int(parts[-1].rstrip())

    def set_pass_monkey(self, pass_note: str):
        parts = pass_note.split(' ')
        self.pass_monkey = int(parts[-1])

    def set_fail_monkey(self, fail_note: str):
        parts = fail_note.split(' ')
        self.fail_monkey = int(parts[-1])

    def test_and_throw_item(self):
        if self.worry_level % self.test_operand == 0:
            if self.print_actions:
                print(f'\t\tCurrent worry level is divisible by {self.test_operand}')
            item = self.throw_to(self.pass_monkey)
            return self.pass_monkey, item
        else:
            if self.print_actions:
                print(f'\t\tCurrent worry level is not divisible by {self.test_operand}')
            item = self.throw_to(self.fail_monkey)
            return self.fail_monkey, item

    def throw_to(self, monkey_id):
        if self.print_actions:
            print(f'\t\tItem with worry level {self.worry_level} is thrown to monkey {monkey_id}')
        return self.worry_level

    def catch(self, item):
        self.items.append(item)

    def inspect(self, item):
        self.num_inspects += 1
        self.worry_level = item
        if self.print_actions:
            print(f'\tMonkey inspects an item with a worry level of {self.worry_level}')

    def do_operation(self):
        self.operation()
    
    def get_bored(self):
        self.worry_level = self.worry_level // 3
        if self.print_actions:
            print(f'\t\tMonkey gets bored with item. Worry level is divided by 3 to {self.worry_level}')

    def done_throwing(self):
        self.items = []
    

def main():
    # lines = aoc_utils.readlines('input\\example11.txt')
    lines = aoc_utils.readlines('input\\day11.txt')

    jungle = Jungle(lines)
    jungle.make_monkeys()
    jungle.monkey_around()
    answer = jungle.calculate_monkey_business()

    print(f'Part 1: {answer}')


if __name__ == '__main__':
    main()
