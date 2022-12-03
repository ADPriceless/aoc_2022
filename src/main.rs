use std::fs;

mod days;
use days::day2;

fn main() {
    // let file_path = "./input/example2a.txt";
    let file_path = "./input/day2.txt";
    let contents = fs::read_to_string(file_path)
        .expect("Could not read file!");

    let answer = day2::part1(&contents);
    println!("Part 1: {answer}");

    let answer = day2::part2(&contents);
    println!("Part 2: {answer}");
}
