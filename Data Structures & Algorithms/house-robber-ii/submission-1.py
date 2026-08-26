class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def func(L, R):
            rob1, rob2 = 0, 0

            for i in range(L, R):
                temp = max(nums[i] + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        return max(func(0, len(nums) - 1), func(1, len(nums)))