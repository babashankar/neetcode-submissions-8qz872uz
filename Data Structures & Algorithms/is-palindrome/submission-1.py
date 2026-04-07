class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            if not self.alphaNum(s[l]):
                l+=1
            elif not self.alphaNum(s[r]):
                r-=1
            elif s[l].lower()==s[r].lower():
                l+=1
                r-=1
            else:
                return False
        return True 
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
        