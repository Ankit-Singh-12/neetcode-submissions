class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])

        minheap = []
        currcap = 0

        for ps, start, end in trips:
            while minheap and minheap[0][0] <= start:
                currcap -= heapq.heappop(minheap)[1]
            
            currcap += ps
            if currcap > capacity:
                return False
            
            heapq.heappush(minheap, [end, ps])
        
        return True