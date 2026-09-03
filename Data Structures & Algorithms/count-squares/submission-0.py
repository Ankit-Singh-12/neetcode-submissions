class CountSquares:

    def __init__(self):
        self.points = []
        self.pntscnt = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.pntscnt[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point

        for dx, dy in self.points:
            if abs(x - dx) != abs(y - dy) or x == dx or y == dy:
                continue 
            res += self.pntscnt[(x, dy)] * self.pntscnt[(dx, y)]
        
        return res
