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


def part1(aoc_input: list[str]) -> int:
    total = 0
    for i, packet in enumerate(aoc_input):
        left_packet = eval(packet.split('\n')[0])
        right_packet = eval(packet.split('\n')[1])
        if compare(left_packet, right_packet):
            total += (i + 1)
            # print(total)
        # print(i, compare(left_packet, right_packet))
    return total


def bubble_sort(all_packets: list) -> None:
    for _ in range(len(all_packets)):
        for i in range(1, len(all_packets)):
            if compare(all_packets[i-1], all_packets[i]) is False: # left > right
                temp = all_packets[i]
                all_packets[i] = all_packets[i-1]
                all_packets[i-1] = temp


def part2(aoc_input: list[str]) -> int:
    all_packets = []
    for packet in aoc_input:
        all_packets.append(eval(packet))
    # insert two additional divider packets
    all_packets.append([[2]])
    all_packets.append([[6]])
    bubble_sort(all_packets)
    decoder_key1 = all_packets.index([[2]]) + 1
    decoder_key2 = all_packets.index([[6]]) + 1
    return decoder_key1 * decoder_key2


def main():
    # aoc_input = aoc_utils.readgroups('input\\example13.txt')
    aoc_input = aoc_utils.readgroups('input\\day13.txt')
    answer = part1(aoc_input)
    print(f'Part 1: {answer}')

    # aoc_input = aoc_utils.readlines('input\\example13.txt', remove_blank_lines=True)
    aoc_input = aoc_utils.readlines('input\\day13.txt', remove_blank_lines=True)
    answer = part2(aoc_input)
    print(f'Part 2: {answer}')



if __name__ == '__main__':
    main()
