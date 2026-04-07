class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        l=len(t)
        res=[0]*l
        st=[]

        for i in range(l-1,-1,-1):
            while st and t[st[-1]]<=t[i]:
                st.pop()
            res[i]=st[-1]-i if st else 0
            st.append(i)
        return res 
        