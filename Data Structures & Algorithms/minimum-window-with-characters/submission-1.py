class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq={}

        for i in t:
            freq[i]=freq.get(i,0)+1
        i,j=0,0
        cnt=len(freq)
        resStr=""
        mini=float("inf")

        while j<len(s):
            if s[j] in freq:
                freq[s[j]]-=1
                if freq[s[j]]==0:
                    cnt-=1
            while cnt==0:
                if mini>j-i+1:
                    mini=j-i+1
                    resStr=s[i:j+1]
                if s[i] in freq:
                    if freq[s[i]]==0:
                        cnt+=1
                    freq[s[i]]+=1
                i+=1
            j+=1
        return resStr
            


        