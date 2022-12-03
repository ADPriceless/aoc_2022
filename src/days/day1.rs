fn count_calories(input: &String) -> Vec<i32>{
    let mut total = 0;
    let mut calories: Vec<i32> = Vec::new();
    for line in input.lines() {
        match line.parse::<i32>() {
            Ok(value) => total = total + value,
            Err(_) => {calories.push(total); total = 0},
        }
    }
    calories.push(total);
    return calories;
}


pub fn part1(input: &String) -> i32 {
    let calories = count_calories(input);
    let max_calories = calories.iter().max().expect("Not an i32!");
    return *max_calories;
}


pub fn part2(input: &String) -> i32 {
    let mut calories = count_calories(input);
    calories.sort(); // lowest-to-highest
    calories.reverse();
    calories[..3].to_vec().iter().sum()
}