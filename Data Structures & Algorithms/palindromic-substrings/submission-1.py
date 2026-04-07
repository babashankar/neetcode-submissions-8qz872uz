class Solution:
    def countSubstrings(self, s: str) -> str:
        d={}
        self.s=0

        def fn(i,j):
            
            
            if i<0 or j==len(s) or s[i]!=s[j]:
                return 0
            
            return 1+fn(i-1,j+1)
        
        maxi,mini=0,0
        maxLen=1

        for i in range(len(s)):
            self.s+=fn(i,i)
            if i+1<len(s):
                self.s+=fn(i,i+1)
        return self.s