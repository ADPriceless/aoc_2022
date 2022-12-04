pub fn part1 (input: &String) -> u32 {
    let mut total = 0;
    for rucksack in input.lines() {
        let (c1, c2) = split_rucksack(rucksack);
        let in_both = find_in_both(c1, c2).pop();
        match in_both {
            Some(item) => total += prioritise(item),
            None => panic!("There should be at least one item in both"),
        }
    }
    total as u32
}

fn split_rucksack(rucksack: &str) -> (&str, &str) {
    let half_length = rucksack.len() / 2;
    return (&rucksack[..half_length], &rucksack[half_length..]);
}

fn find_in_both(c1: &str, c2: &str) -> String {
    if c1.len() == 0 || c2.len() == 0 {
        panic!("Both compartments must contain items!");
    }
    let mut in_both = String::new();
    for item1 in c1.chars() {
        // check in item1 in c2 but ignore items already found in both
        if c2.contains(item1) && !in_both.contains(item1) {
            in_both.insert(0, item1);
        }
    }
    return in_both;
}

fn prioritise(item: char) -> u32 {
    if !item.is_alphabetic() {
        panic!("item must be alphabetic!");
    }
    if item.is_ascii_uppercase() {
        return item as u32 - 38;
    }
    else if item.is_ascii_lowercase() {
        return item as u32 - 96;
    }
    0 // return 0 if not alphabetical
}

pub fn part2 (input: &String) -> u32 {
    let mut total = 0;
    let rucksacks = Vec::from_iter(input.lines());
    for group in rucksacks.chunks(3) {
        let in_first_two = find_in_both(group[0], group[1]);
        let in_all_three = find_in_both(&in_first_two[..], group[2]).pop();
        match in_all_three {
            Some(item) => total += prioritise(item),
            None => panic!("There should be an item in all three rucksacks"),
        }
    }
    return total;
}
