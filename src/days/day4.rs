pub fn part1 (input: &String) -> u32 {
    let mut count = 0;
    for sections in input.lines() {
        let bounds = get_bounds(sections);
        // let (lb1, ub1, lb2, ub2) = get_bounds(sections);
        let lb1 = bounds[0]; // println!("{lb1}");
        let ub1 = bounds[1]; // println!("{ub1}");
        let lb2 = bounds[2]; // println!("{lb2}");
        let ub2 = bounds[3]; // println!("{ub2}");

        let s1_contains_s2 = contains(lb1, ub1, lb2, ub2);
        let s2_contains_s1 = contains(lb2, ub2, lb1, ub1);
        if s1_contains_s2 || s2_contains_s1 {
            count = count + 1;
        }
    }
    return count;
}

fn get_bounds(sections: &str) -> Vec<u32> {
    let mut all_bounds = Vec::new();
    let subsections = sections.split(",");
    for subsection in subsections {
        let bounds = subsection.split("-");
        for bound in bounds {
            match bound.parse::<u32>() {
                Ok(value) => all_bounds.push(value),
                Err(_) => panic!("Bound is not a number!"),
            };
        }
    }
    return all_bounds;
}

fn contains(lb1: u32, ub1: u32, lb2: u32, ub2: u32) -> bool {
    lb1 <= lb2 && ub1 >= ub2
}

pub fn part2 (input: &String) -> u32 {
    let mut count = 0;
    for sections in input.lines() {
        let bounds = get_bounds(sections);
        let lb1 = bounds[0]; // println!("{lb1}");
        let ub1 = bounds[1]; // println!("{ub1}");
        let lb2 = bounds[2]; // println!("{lb2}");
        let ub2 = bounds[3]; // println!("{ub2}");

        let s1_contains_s2 = contains(lb1, ub1, lb2, ub2);
        let s2_contains_s1 = contains(lb2, ub2, lb1, ub1);
        if s1_contains_s2 || s2_contains_s1 || overlaps(lb1, ub1, lb2, ub2) {
            count = count + 1;
        }
    }
    return count;
}

fn overlaps (lb1: u32, ub1: u32, lb2: u32, ub2: u32) -> bool {
    ((lb1 <= lb2) && (lb2 <= ub1)) || ((lb1 <= ub2) && (ub2 <= ub1))
}
