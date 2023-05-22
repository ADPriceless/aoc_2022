enum Parent<'a> {
    None,
    Some(&'a Directory<'a>)
}

struct Directory<'a> {
    name: &'a str,
    parent: Parent<'a>,
    children: Vec<&'a Directory<'a>>,
    size: u32
}

impl <'a>Directory<'a> {
    pub fn new(name: &'a str, parent: Parent<'a>) -> Self {
        Self {
            name,
            parent,
            children: Vec::<&Directory<'a>>::new(),
            size: 0
        }
    }

    pub fn add_parent(mut self, parent: &Directory) {}

    pub fn add_child(&mut self, child: &'a Directory<'a>) {
        self.children.push(child);
    }
    
    pub fn add_to_size(&mut self, value: u32) {
        self.size += value;
    }

}

struct FileTree<'a> {
    directories: Vec<&'a Directory<'a>>
}


pub fn part1(input: String) {

    let root = Directory::new("/", Parent::None);
    let mut current_dir = &root;

    let lines = input.split("\n");
    for line in lines {
        if line.starts_with("$ cd") {
            let cd_to = line.split(" ").last().unwrap();
            // if directory == "/"
                // go to top directory: reset file pointer to top
            if cd_to == "/" {
                current_dir = &root;
            }
            // else if directory is ..
                // new current directory is parent of current directory
            else if cd_to == ".." {
                current_dir = match current_dir.parent {
                    Parent::None => current_dir,
                    Parent::Some(directory) => directory
                };
            }
            // else if directory is some string
                // move to that directory
            else {
                for child in current_dir.children.iter() {
                    if child.name == cd_to {
                        current_dir = *child;
                        break;
                    }
                }
            }
        }
        // else if command is 'ls'
            // basically, ignore since the commands after will be dir or a filename
        else if line.starts_with("$ ls") {
            // do nothing
        }
        // else if command starts with "dir"
            // add the subdirectory to the current directory's children
        else if line.starts_with("dir") {
            let name = line.split(" ").last().unwrap();
            let parent = Parent::Some(current_dir);
            let child = Directory::new(name, parent);
            current_dir.add_child(&child);
        }
        // else if command starts with a number
            // add that value to the directory size
        else if line.chars().next().unwrap().is_numeric() {
            let file_size = line.split(" ").next().unwrap().parse::<u32>().unwrap();
            current_dir.add_to_size(file_size);
        }
    }
}