class Solution:
    def climbStairs(self, n: int) -> int:
        
        f1 = 1
        f2 = 1

        for i in range(2, n + 1):
            temp = f1 + f2
            f1 = f2
            f2 = temp
        
        return f2