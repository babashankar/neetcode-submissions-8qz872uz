class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        visited=[False for _ in range(n)]

        graph={i :[] for i in range(n)}
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)


        def dfs(i,parent):
            visited[i]=True

            for node in graph[i]:
        
                if visited[node]:
                    if node!=parent:
                        return True
                else:
                    if dfs(node,i):
                        return True
            return False
        if dfs(0,-1):
            return False
        return False if False in visited else True
                

            
        