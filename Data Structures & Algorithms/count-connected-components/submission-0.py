class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=[False]*n

        adj={i:[] for i in range(n)}
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)



        def dfs(node):
            if visited[node]:
                return 
            visited[node]=True
            for i in  adj[node]:
                dfs(i)
        c=0
        for i in adj:
            if not visited[i]:
                c+=1
                dfs(i)
        return c





        