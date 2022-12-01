use std::fs;

fn main() {
    // let file_path = "./input/example1a.txt";
    let file_path = "./input/day1.txt";
    let contents = fs::read_to_string(file_path)
        .expect("Could not read file!");

    let mut elf_calories: Vec<i32> = Vec::new();
    let mut total = 0;
    for line in contents.lines() {
        match line.parse::<i32>() {
            Ok(value) => total = total + value,
            Err(_) => {elf_calories.push(total); total = 0},
        }
    }
    let max_calories = elf_calories.iter().max().expect("Not an i32!");
    println!("{max_calories}");
}
