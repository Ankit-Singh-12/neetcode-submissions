class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        visit = set(deadends)
        q = deque([("0000", 0)])

        def children(num):
            res = []
            for i in range(4):
                v1 = (int(num[i]) + 1) % 10
                res.append(num[:i] + str(v1) + num[i + 1:]) 
                v2 = (int(num[i]) - 1) % 10
                res.append(num[:i] + str(v2) + num[i + 1:])

            return res

        while q:
            lock, turn = q.popleft()
            if lock == target:
                return turn

            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append((child, turn + 1))

        return -1 