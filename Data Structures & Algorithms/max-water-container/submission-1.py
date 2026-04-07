class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1

        maxi=0
        while l<r:
            a=min(heights[l],heights[r])
            maxi=max(maxi,a*(r-l))
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return maxi


        