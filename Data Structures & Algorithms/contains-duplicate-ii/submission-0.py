class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}

        for i, n in enumerate(nums):
            if n in hm:
                if abs(hm[n] - i) <= k:
                    return True
            hm[n] = i
        
        return False