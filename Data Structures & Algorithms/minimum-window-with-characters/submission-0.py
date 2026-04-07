class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l=len(s)
        d={}

        for i in t:
            if i not in d:
                d[i]=0
            d[i]+=1
        cnt=len(d)
        mini=float("inf")
        start,end=0,0
        i,j=0,0
        while j<l:
            if s[j] in d:
                d[s[j]]-=1
                if d[s[j]]==0:
                    cnt-=1
            while cnt==0:
                if j-i+1<mini:
                    mini=j-i+1
                    start,end=i,j
                if s[i] in d:
                    if d[s[i]]==0:
                        cnt+=1
                    d[s[i]]+=1
                i+=1
            j+=1
        return s[start:end+1] if mini!=float("inf") else ""
                


        