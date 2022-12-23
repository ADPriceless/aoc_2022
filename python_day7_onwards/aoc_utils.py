def readlines(
    filepath: str, 
    remove_blank_lines: bool = False,
    remove_trailing_newline: bool = False
) -> list[str]:
    with open(filepath) as f:
        lines = f.readlines()
    if remove_blank_lines:
        lines = filter(lambda line: line != '\n', lines)
    if remove_trailing_newline:
        lines = [line.rstrip() for line in lines]
    return lines


def readgroups(filepath: str) -> list[str]:
    with open(filepath) as f:
        text = f.read()
    return text.split('\n\n')


def split_and_cast(line: str, split=' ') -> list:
    result = []
    for term in line.split(split):
        stripped = term.strip()
        if stripped.isnumeric():
            result.append(int(stripped))
        elif stripped[0] == '-' and stripped[1:].isnumeric():
            result.append(int(stripped))
        else:
            result.append(stripped)
    return result


class Point2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
