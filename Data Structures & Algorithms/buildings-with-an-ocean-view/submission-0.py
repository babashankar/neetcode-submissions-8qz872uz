class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        l=len(heights)
        maxi=heights[-1]
        res=[l-1]

        for i in range(l-2,-1,-1):
            if heights[i]>maxi:
                res.append(i)
                maxi=heights[i]
        return res[::-1]
        