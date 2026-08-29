class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, currsum = 0, 0
        prefix = defaultdict(int)
        prefix[0] = 1

        for num in nums:
            currsum += num
            diff = currsum - k

            res += prefix[diff]
            prefix[currsum] += 1
        
        return res