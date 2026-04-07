class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet=set(wordDict)
        d={}

        def fn(s):
            if s in d:
                return d[s]
            if s=="":
                return True
            for i in range(len(s)):
                
                if s[:i+1] in wordSet:
                    if fn(s[i+1:]):
                        d[s]=True
                        return True
            d[s]=False
            return False
        return fn(s)
        