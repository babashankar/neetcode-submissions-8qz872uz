class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=len(s)
        def fn(i,j):
            while i>=0 and j<l and s[i]==s[j]:
                i-=1
                j+=1
            return i+1,j-1

        maxLen=0
        start,end=0,0
        
        for i in range(l):
            a,b=fn(i-1,i+1)
            c,d=fn(i,i+1)
            if b-a+1>maxLen:
                maxLen=b-a+1
                start,end=a,b
            if d-c+1>maxLen:
                maxLen=d-c+1
                start,end=c,d
        return s[start:end+1]



        