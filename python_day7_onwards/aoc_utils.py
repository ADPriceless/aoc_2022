def readlines(filepath: str) -> list[str]:
    with open(filepath) as f:
        lines = f.readlines()
    return lines


class Point2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
