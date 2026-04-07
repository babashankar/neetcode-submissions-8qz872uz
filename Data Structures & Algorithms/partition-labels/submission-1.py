class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={}
        l=len(s)

        for i in range(l):
            d[s[i]]=i
        prev=-1
        res=[]
        maxi=-1
        for i in range(len(s)):
            maxi=max(maxi,d[s[i]])
            if maxi==i:
                res.append(i-prev)
                prev=i  
        return res



        