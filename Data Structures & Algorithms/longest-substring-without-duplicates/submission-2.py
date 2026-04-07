class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i,j=0,0
        maxi=0
        seti=set()

        while j<len(s):
    

            while s[j] in seti:
                seti.remove(s[i])
                i+=1
            seti.add(s[j])
            maxi=max(maxi,j-i+1)
            j+=1
        return maxi


            
        