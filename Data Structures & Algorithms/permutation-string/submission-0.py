
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1=len(s1)
        l2=len(s2)

       

        d={}
        for i in s1:
            if i not in d:
                d[i]=0
            d[i]+=1
        unique=len(d)
        i,j=0,0

        while j<l2:
            if s2[j] in d:
                d[s2[j]]-=1
                if d[s2[j]]==0:
                    unique-=1
            if j-i+1==l1:
                if unique==0:
                    return True
                if s2[i] in d:
                    if d[s2[i]]==0:
                        unique+=1
                    d[s2[i]]+=1
                i+=1
            j+=1
        return False

        