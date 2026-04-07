class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited=[False for _ in range(n)]
        graph={i:[] for i in range(n)}
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        def dfs(i,parent):
            visited[i]=True



            for nei in graph[i]:
                if visited[nei] and nei!=parent:
                    return True
                if not visited[nei] and dfs(nei,i):
                    return True
            return False
        c=0
        for i in range(n):
            if not visited[i]:
                c+=1
                if dfs(i,-1):
                    return False
        return c==1

        