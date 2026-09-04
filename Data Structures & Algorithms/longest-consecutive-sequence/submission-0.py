class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        res = 0

        for n in hs:
            l = 1
            if n - 1 not in hs:
                while n + l in hs:
                    l += 1
                res = max(res, l)
        
        return res