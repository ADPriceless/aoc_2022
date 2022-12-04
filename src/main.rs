mod aoc_common;
mod days;
use days::day4;

fn main() {
    // let input = aoc_common::read_input("./input/example4.txt");
    let input = aoc_common::read_input("./input/day4.txt");
    
    let answer = day4::part1(&input);
    println!("Part 1: {answer}");

    let answer = day4::part2(&input);
    println!("Part 2: {answer}");
}
