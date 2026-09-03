class Solution:
    def isHappy(self, n: int) -> bool:
        def square(num):
            summ = 0
            while num:
                summ += (num % 10) ** 2
                num //= 10
            return summ
        
        slow = square(n)
        fast = square(square(n))

        while slow != fast:
            slow = square(slow)
            fast = square(square(fast))
        
        return slow == 1