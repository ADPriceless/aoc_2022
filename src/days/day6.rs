use std::collections::HashSet;
use core::hash::Hash;


pub fn part1 (input: &String) -> usize {
    const MARKER_LEN: usize = 4;
    find_marker_end_idx(input, MARKER_LEN)
}


fn find_marker_end_idx(input: &String, marker_len: usize) -> usize {
    for line in input.lines() { // only one line this time
        let length = line.len();
        for start in 0..length-marker_len {
            let char_range = get_char_range(line, start, marker_len);
            if has_unique_elements(char_range.chars()) {
                return start + marker_len;
            }
        }
    }
    0
}


fn get_char_range(string_slice: &str, start: usize, length: usize) -> String {
    let mut char_range = String::new();
    for (i, ch) in string_slice.char_indices() {
        if start <= i && i < start + length {
            char_range.push(ch);
        }
    }
    return char_range;
}


// Shamelessly stolen from https://stackoverflow.com/questions/46766560/how-to-check-if-there-are-duplicates-in-a-slice
fn has_unique_elements<T>(iter: T) -> bool
where
    T: IntoIterator,
    T::Item: Eq + Hash,
{
    let mut uniq = HashSet::new();
    iter.into_iter().all(move |x| uniq.insert(x))
}


pub fn part2 (input: &String) -> usize {
    const MARKER_LEN: usize = 14;
    find_marker_end_idx(input, MARKER_LEN)
}