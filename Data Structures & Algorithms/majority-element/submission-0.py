class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = cnt = 0

        for n in nums:
            if cnt == 0:
                res = n
            cnt += 1 if res == n else -1
        
        return res