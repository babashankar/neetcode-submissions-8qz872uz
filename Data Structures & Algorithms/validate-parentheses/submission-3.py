class Solution:
    def isValid(self, s: str) -> bool:
        d={")":"(","]":"[","}":"{"}
        st=[]


        for i in s:
            if i not in d:
                st.append(i)
            else:
                if not st:
                    return False
               
                if st[-1]!=d[i]: 
                    return False
                st.pop()
        return len(st)==0
        