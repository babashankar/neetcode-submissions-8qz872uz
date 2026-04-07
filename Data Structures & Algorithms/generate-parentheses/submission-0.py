class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def fun(pref,i,j):
            if i>j:
                return
            if i==0:
                res.append(pref+')'*j)
                return
            fun(pref+'(',i-1,j)
            fun(pref+')',i,j-1)
        fun("",n,n)
        return res


        