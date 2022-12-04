mod aoc_common;
mod days;
use days::day3;

fn main() {
    // let input = aoc_common::read_input("./input/example3.txt");
    let input = aoc_common::read_input("./input/day3.txt");
    
    let answer = day3::part1(&input);
    println!("Part 1: {answer}");

    let answer = day3::part2(&input);
    println!("Part 2: {answer}");
}
