"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import defaultdict 
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        timeline = defaultdict(int)

        for interval in intervals:
            timeline[interval.start] += 1
            timeline[interval.end] -= 1 
        
        current = 0
        min_rooms = 0 

        for time in sorted(timeline):
            current += timeline[time]
            min_rooms = max(current, min_rooms)
        return min_rooms

