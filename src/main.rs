mod aoc_common;
mod days;
use days::day7;

fn main() {
    let input = aoc_common::read_input("./input/example7.txt");
    // let input = aoc_common::read_input("./input/day7.txt");

    let answer = day7::part1(input);
}
