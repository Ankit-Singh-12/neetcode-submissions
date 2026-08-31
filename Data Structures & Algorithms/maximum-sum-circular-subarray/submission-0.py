class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currmax, currmin = 0, 0
        maxs, mins = nums[0], nums[0]
        total = 0

        for n in nums:
            currmax = max(currmax + n, n)
            maxs = max(maxs, currmax)
            currmin = min(currmin + n, n)
            mins = min(mins, currmin)
            total += n
        
        return max(maxs, total - mins) if maxs > 0 else maxs