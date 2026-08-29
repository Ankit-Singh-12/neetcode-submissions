class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, currsum = 0, 0
        prefix = {0 : 1}

        for num in nums:
            currsum += num
            diff = currsum - k

            res += prefix.get(diff, 0)
            prefix[currsum] = prefix.get(currsum, 0) + 1
        
        return res