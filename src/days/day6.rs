pub fn part1 (input: &String) -> usize {
    for line in input.lines() { // only one line this time
        // let idx = line.find(no_duplicate(a, b, c, d));
        let length = line.len();
        let chars = line.as_bytes();
        for i in 0..length {
            if no_duplicate(chars[i], chars[i+1], chars[i+2], chars[i+3]) {
                return i+4;
            }
        }
    }
    0
}


fn no_duplicate (a: u8, b: u8, c: u8, d: u8) -> bool{
    a != b && a != c && a != d && b != c && b != d && c != d
}