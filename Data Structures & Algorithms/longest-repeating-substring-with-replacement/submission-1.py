class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,j=0,0
        l=len(s)

        d={}
        maxi=0
        maxf=0

        while j<l:
            if s[j] not in d:
                d[s[j]]=0
            d[s[j]]+=1
            maxf=max(maxf,d[s[j]])

            while (j-i+1)-maxf>k:
                d[s[i]]-=1
                if d[s[i]]==0:
                    del d[s[i]]
                i+=1    
            maxi=max(maxi,j-i+1)
            j+=1
        return maxi
        