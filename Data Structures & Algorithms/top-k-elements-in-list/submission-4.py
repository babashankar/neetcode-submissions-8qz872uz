class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d={i:0 for i in nums}
        l=len(nums)

        for i in nums:
            d[i]+=1
        buck=[[] for i in range(l+1)]

        for i in d:
            buck[d[i]].append(i)
        
        i=l
        res=[]
        while i>=0 and k>0:
            res+=buck[i]
            k-=len(buck[i])
            i-=1
        return res


        