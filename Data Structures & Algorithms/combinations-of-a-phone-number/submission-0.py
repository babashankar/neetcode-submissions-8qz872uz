class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        d={str(i):[] for i in range(2,10)}
        
        i=0
        num=2
        while i<23:
            tmp=i

            if str(num) in "79":
                i+=4
            else:
                i+=3
            d[str(num)]=[tmp,i]
            num+=1
        res=[]
        self.l=len(digits)



        def fun(i,pref):
            if i==self.l:
                res.append(pref)
                return
            curr=digits[i]
            l,h=d[curr]
            for comb in range(l,h):
                act=chr(ord('a')+comb)
                fun(i+1,pref+act)
        fun(0,"")
        return res



        