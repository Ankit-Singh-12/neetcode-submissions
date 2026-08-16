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

        for pair in intervals:
            if pair.start >= lastend:
                lastend = pair.end
            else:
                return False
        
        return True