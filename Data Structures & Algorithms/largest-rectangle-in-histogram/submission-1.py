class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def PLR(arr):
            l=len(arr)
            st=[]
            res=[-1]*l

            for i in range(l):
                while st and arr[st[-1]]>=arr[i]:
                    st.pop()
                if st:
                    res[i]=st[-1]
                st.append(i)
            return res
        def NLR(arr):
            l=len(arr)
            st=[]
            res=[l]*l

            for i in range(l-1,-1,-1):
                while st and arr[st[-1]]>=arr[i]:
                    st.pop()
                if st:
                    res[i]=st[-1]
                st.append(i)
            return res
        a=PLR(heights)
        b=NLR(heights)
        maxi=0

        for i in range(len(heights)):
            maxi=max(maxi,(b[i]-a[i]-1)*heights[i])
        return maxi

        