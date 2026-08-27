class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []

    def addNum(self, num: int) -> None:
        if self.large and self.large[0] < num:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        if len(self.large) > len(self.small) + 1:
            n1 = -heapq.heappop(self.large)
            heapq.heappush(self.small, n1)
        elif len(self.small) > len(self.large) + 1:
            n2 = -heapq.heappop(self.small)
            heapq.heappush(self.large, n2)

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (self.large[0] + -self.small[0]) / 2
        