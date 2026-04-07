class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited=[0]*numCourses

        def adj(l):
            d={i:[] for i in range(numCourses)}
            for i,j in l:
                d[j].append(i)
            return d
        self.c=0
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
            self.c+=1
            visited[k]=2
            return True
        for i in adjList:
            if visited[i]==0:
                if not dfs(i):
                    return False
        if self.c!=numCourses:
            return False
        return True
        