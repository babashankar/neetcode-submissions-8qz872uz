class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={}

        for i in s:
            d[i]=d.get(i,0)+1
        prev=-1
        seen=set()
        res=[]
        for i in range(len(s)):
            seen.add(s[i])
            d[s[i]]-=1
            if d[s[i]]==0:
                seen.remove(s[i])

            if d[s[i]]==0 and len(seen)==0:
                res.append(i-prev)
                prev=i
        return res



        