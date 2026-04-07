class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        d={}
        maxi=0
        while j<len(s):
            if s[j] in d:
                if d[s[j]]>=i:
                    i=d[s[j]]+1
            d[s[j]]=j
            maxi=max(j-i+1,maxi)
            j+=1
        return maxi
        
        