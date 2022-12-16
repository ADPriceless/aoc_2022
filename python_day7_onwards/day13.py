import aoc_utils


def compare(left, right):
    left_is_list = isinstance(left, list)
    right_is_list = isinstance(right, list)

    # if both are list then look at each item in the list and compare
    if left_is_list and right_is_list:
        # loop over and compare:
        i = 0
        while i < len(left) and i < len(right):
            result = compare(left[i], right[i])
            if result is True:
                return True
            elif result is False:
                return False
            else: # result is None
                i += 1
        # if reach the end of left first: then return correct
        if i == len(left) and i == len(right):
            return None #?
        elif i == len(left) and i < len(right):
            return True
        else: # right ran out first
            return False
    elif left_is_list and not right_is_list:
        result = compare(left, [right])
        if result is True:
            return True
        elif result is False:
            return False
        # else: result is None
    elif not left_is_list and right_is_list:
        result = compare([left], right)
        if result is True:
            return True
        elif result is False:
            return False
        # else: result is None
    else:
        if left < right:
            return True
        elif left == right: # continue comparing
            return None
        else: # right > left
            return False


def solve(aoc_input: list[str]) -> int:
    total = 0
    for i, packet in enumerate(aoc_input):
        left_packet = eval(packet.split('\n')[0])
        right_packet = eval(packet.split('\n')[1])
        if compare(left_packet, right_packet):
            total += (i + 1)
            print(total)
        # print(i, compare(left_packet, right_packet))
    return total


def main():
    # aoc_input = aoc_utils.readgroups('input\\example13.txt')
    aoc_input = aoc_utils.readgroups('input\\day13.txt')
    answer = solve(aoc_input)
    print(f'Part 1: {answer}')

if __name__ == '__main__':
    main()
