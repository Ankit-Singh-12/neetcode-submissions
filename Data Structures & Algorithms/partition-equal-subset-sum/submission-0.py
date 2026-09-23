class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            if num > target:
                return False
            
            for i in range(target, num - 1, -1):
                if dp[i - num]:
                    dp[i] = True
            
            if dp[target]:
                return True
        
        return dp[target]