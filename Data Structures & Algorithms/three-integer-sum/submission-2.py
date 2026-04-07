class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res=[]
        l=len(nums)
        nums.sort()


        for i in range(l-2):
            if i>0 and nums[i]==nums[i-1]:
                continue

            start=i+1
            end=l-1

            while start<end:
                a=nums[i]+nums[start]+nums[end]
                if a==0:
                    res.append([nums[i],nums[start],nums[end]])
                    start+=1
                    end-=1
                    while start<end and nums[start]==nums[start-1]:
                        start=start+1
                    while  start<end and nums[end]==nums[end+1]:
                        end=end-1
                elif a<0:
                    start+=1
                else:
                    end-=1
        return res

        