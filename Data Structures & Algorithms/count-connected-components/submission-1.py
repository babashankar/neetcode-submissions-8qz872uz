class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=[False for _ in range(n)]
        d={i:[] for i in range(n)}
        for i,j in edges:
            d[i].append(j)
            d[j].append(i)


        def dfs(i):
            if visited[i]:
                return 
            visited[i]=True

            for neigh in d[i]:
                dfs(neigh)
        c=0
        for i in range(n):
            if visited[i]:
                continue
            c+=1
            dfs(i)
        return c
        