pub fn part1 (input: &String) -> String {
    let mut top_crates = String::new();
      
    let mut stacks = initialise_stacks(input);
    for line in input.lines() {
        match parse_move(line) {
            Some((num_crates, from, to)) => {
                do_move(&mut stacks, num_crates, from, to);
            },
            _ => print!(""),
        }
    }

    for mut stack in stacks {
        match stack.pop() {
            Some(ch) => top_crates.push(ch),
            None => panic!("No value to pop"),
        }
    }

    return top_crates;
}


fn initialise_stacks (input: &String) -> Vec<Vec<char>> {
    let mut stacks: Vec<Vec<char>> = Vec::new();
    let first_line = match input.lines().next() {
        Some(value) => value,
        None => "",
    };
    let num_stacks = (first_line.len() + 1) / 4;
    for _ in 0..num_stacks {
        stacks.push(Vec::new())
    }
    for line in input.lines() {
        if line.starts_with("move") {
            break;
        }
        for (idx, ch) in line.chars().enumerate() {
            if idx % 4 == 1 {
                if ch.is_numeric() {
                    break;
                }
                if ch != ' ' {
                    let stack_idx = idx / 4;
                    stacks[stack_idx].push(ch)
                }
            }
        }
    }
    for stack_idx in 0..num_stacks {
        stacks[stack_idx].reverse();
    }
    return stacks;
}

fn parse_move (line: &str) -> Option<(usize, usize, usize)> {
    let mut commands: Vec<usize> = Vec::new();
    if line.starts_with("move") {
        for term in line.split(" ") {
            match term.parse::<usize>() {
                Ok(value) => commands.push(value),
                Err(_) => print!(""),
            };

        }
        Some((commands[0], commands[1]-1, commands[2]-1))
    }
    else {
        None
    }
}

fn do_move (stacks: &mut Vec<Vec<char>>, num_crates: usize, from: usize, to: usize) {
    for _ in 0..num_crates {
        match stacks[from].pop() {
            Some(value) => stacks[to].push(value),
            None => panic!("Ran out of crates!"),
        }
    }
}

pub fn part2 (input: &String) -> String {
    let mut top_crates = String::new();

    let mut stacks = initialise_stacks(input);
    for line in input.lines() {
        match parse_move(line) {
            Some((num_stacks, from, to)) => {
                do_move_9001(&mut stacks, num_stacks, from, to);
            },
            _ => print!(""),
        }
    }

    for mut stack in stacks {
        match stack.pop() {
            Some(ch) => top_crates.push(ch),
            None => panic!("No value to pop"),
        }
    }

    return top_crates;
}

fn do_move_9001 (stacks: &mut Vec<Vec<char>>, num_crates: usize, from: usize, to: usize)  {
    let mut temp_stack: Vec<char> = Vec::new();
    for _ in 0..num_crates {
        match stacks[from].pop() {
            Some(value) => temp_stack.push(value),
            None => panic!("Ran out of crates!"),
        }
    }
    temp_stack.reverse();
    for value in temp_stack {
        stacks[to].push(value)
    }
}