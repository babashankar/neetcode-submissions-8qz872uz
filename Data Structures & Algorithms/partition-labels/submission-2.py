class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={}
        l=len(s)

        for i in range(l):
            d[s[i]]=i
        lastParsed=-1
        target=d[s[0]]
        res=[]
        for i in range(l):
            target=max(target,d[s[i]])
            if target==i:
                res.append(target-lastParsed)
                lastParsed=target
        return res




        