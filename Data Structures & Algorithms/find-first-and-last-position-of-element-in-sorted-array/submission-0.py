class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarys(nums, target, leftbias):
            l, r = 0, len(nums) - 1
            i = -1
            while l <= r:
                m = l + (r - l) // 2

                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    i = m
                    if leftbias:
                        r = m - 1
                    else:
                        l = m + 1
        
            return i

        left = binarys(nums, target, True)
        right = binarys(nums, target, False)
        return [left, right]
    
        
