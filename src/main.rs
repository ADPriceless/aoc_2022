mod aoc_common;
mod days;
use days::day6;

fn main() {
    // let input = aoc_common::read_input("./input/example5.txt");
    let input = aoc_common::read_input("./input/day6.txt");

    let answer = day6::part1(&input);
    println!("Part 1: {answer}");

    let answer = day6::part2(&input);
    println!("Part 2: {answer}");
}
