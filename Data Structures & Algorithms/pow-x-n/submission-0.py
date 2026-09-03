class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        power = abs(n)

        while power:
            if power % 2:
                res *= x
            x *= x
            power //= 2
        
        return res if n >= 0 else 1 / res