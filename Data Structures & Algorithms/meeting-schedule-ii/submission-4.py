"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        h=[]
        intervals.sort(key=lambda x: x.start)


        for interval in intervals:

            if  h and h[0]<=interval.start:
                heapq.heappop(h)
            heapq.heappush(h,interval.end)
        return len(h)
        