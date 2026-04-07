class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited=[0]*numCourses

        def adj(l):
            d={i:[] for i in range(numCourses)}
            for i,j in l:
                d[j].append(i)
            return d
        st=[]
        adjList=adj(prerequisites)
        print(adjList)

        def dfs(k):
            if visited[k]==1:
                return False
            if visited[k]==2:
                return True
            visited[k]=1
            print(k)

            for ne in adjList[k]:
                if not dfs(ne):
                    return False
            st.append(k)
            visited[k]=2
            return True
        for i in adjList:
            if visited[i]==0:
                if not dfs(i):
                    return []
        if len(st)!=numCourses:
            return []
        return st[::-1]
        