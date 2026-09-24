class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)

        for num in sorted(count):
            val = count[num]

            if val > 0:
                for start in range(num, num + groupSize):
                    count[start] -= val
                    if count[start] < 0:
                        return False
        
        return True