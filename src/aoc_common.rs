use std::fs;

pub fn read_input(file_path: &str) -> String {
    fs::read_to_string(file_path)
        .expect("Could not read file!")
}