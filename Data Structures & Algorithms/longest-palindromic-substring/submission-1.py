class Solution:
    def longestPalindrome(self, s: str) -> str:

        def fn(i,j):
            if i<0 or j==len(s) or s[i]!=s[j]:
                return i+1,j-1
            return fn(i-1,j+1)
        
        maxi,mini=0,0
        maxLen=1

        for i in range(len(s)):
            a,b=fn(i,i)
            if b-a+1>maxLen:
                maxLen=b-a+1
                maxi,mini=a,b
            if i+1<len(s):
                a,b=fn(i,i+1)
                if b-a+1>maxLen:
                    maxLen=b-a+1
                    maxi,mini=a,b
        return s[maxi:mini+1]


        