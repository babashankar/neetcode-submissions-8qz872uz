class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}

        i,j=0,0
        res=0

        while j<len(s):
            if s[j] in d and d[s[j]]>=d[s[i]]:
                i=d[s[j]]+1
            d[s[j]]=j
            res=max(res,j-i+1)
            j+=1
        return res
        