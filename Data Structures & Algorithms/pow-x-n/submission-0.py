class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n==0:
            return 1
        if n<0:
            n=-n
            x=1/x
        half=self.myPow(x,n//2)
        if n&1==1:
            return x*half*half
        return half*half
    
        