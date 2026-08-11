"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        lastend = -math.inf
        intervals.sort(key=lambda i:i.start)

        for i in intervals:
            if lastend <= i.start:
                lastend = i.end
            else:
                return False
        
        return True
