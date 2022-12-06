mod aoc_common;
mod days;
use days::day5;

fn main() {
    // let input = aoc_common::read_input("./input/example5.txt");
    let input = aoc_common::read_input("./input/day5.txt");

    let answer = day5::part1(&input);
    println!("Part 1: {answer}");

    let answer = day5::part2(&input);
    println!("Part 2: {answer}");
}
