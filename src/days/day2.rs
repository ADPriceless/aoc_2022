use std::collections::HashMap;

fn do_strategy(input: &String, scoring: HashMap<&str, i32>) -> i32{
    let mut total_score = 0;
    for line in input.lines() {
        match scoring.get(line) {
            Some(score) => total_score += score,
            None => println!("Not found!")
        }
    }
    return total_score;
}

pub fn part1(input: &String) -> i32 {
    let strategy = HashMap::from([
        ("A X", 4), // A, X = rock, 1 pt
        ("A Y", 8), // B, Y = paper, 2 pts
        ("A Z", 3), // C, Z = scissors, 3 pts
        ("B X", 1), // win += 6 pts
        ("B Y", 5), // draw += 3 pts
        ("B Z", 9),
        ("C X", 7),
        ("C Y", 2),
        ("C Z", 6),
    ]);
    do_strategy(input, strategy)
}

pub fn part2(input: &String) -> i32 {
    let new_strategy = HashMap::from([
        ("A X", 3), // X = lose
        ("A Y", 4), // Y = draw
        ("A Z", 8), // Z = win
        ("B X", 1), // win += 6 pts
        ("B Y", 5), // draw += 3 pts
        ("B Z", 9),
        ("C X", 2),
        ("C Y", 6),
        ("C Z", 7),
    ]);
    do_strategy(input, new_strategy)
}