class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        d={i:[] for i in range(numCourses)}

        for i,j in prerequisites:
            d[j].append(i)
        visited=[0 for _ in range(numCourses)]



        def dfs(i):
            if visited[i]==2:
                return False
            if visited[i]==1:
                return True
            visited[i]=1

            for neig in d[i]:
                if dfs(neig):
                    return True
            visited[i]=2
            return False
        for i in range(numCourses):
            if visited[i]==0:
                if dfs(i):
                    return False
        return True
            

        
        