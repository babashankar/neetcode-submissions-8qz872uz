class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[intervals[0]]
        


        for i,ele in enumerate(intervals):
            lastEnd=res[-1][1]
            start,end=ele[0],ele[1]

            if start<=lastEnd:
                res[-1][1]=max(lastEnd,end)
            else:
                res.append(intervals[i])
        return res



