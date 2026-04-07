class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        self.res=[]
        n=len(nums)
        self.tmp=[]

        def fn(sumi,i):
            if sumi==0:
                self.res.append(self.tmp[:]) 
                return
            if i==n or sumi<0:
                return
            self.tmp.append(nums[i])
            fn(sumi-nums[i],i)
            self.tmp.pop()
            fn(sumi,i+1)
        fn(target,0)
        return self.res
        