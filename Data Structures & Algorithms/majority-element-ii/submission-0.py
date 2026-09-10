class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1, n2 = 0, 0
        cnt1, cnt2 = 0, 0

        for n in nums:
            if n1 == n:
                cnt1 += 1
            elif n2 == n:
                cnt2 += 1
            elif cnt1 == 0:
                n1 = n
                cnt1 += 1
            elif cnt2 == 0:
                n2 = n
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
            
        cnt1, cnt2 = 0, 0
        for n in nums:
            if n == n1:
                cnt1 += 1
            elif n == n2:
                cnt2 += 1
        
        res = []
        if cnt1 > len(nums) // 3:
            res.append(n1)
        if cnt2 > len(nums) // 3:
            res.append(n2)
        
        return res