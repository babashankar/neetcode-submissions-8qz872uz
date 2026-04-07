class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # Build adjacency list for undirected graph
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        p=[]

        def dfs(node, parent):
            visited[node] = True

            for nei in graph[node]:
                if not visited[nei]:
                    p.append(node)
                    if dfs(nei, node):
                        return True
                # If neighbor is visited and NOT parent → cycle
                elif nei != parent:
                    return True

            return False

        
        return not dfs(0,-1) and visited.count(True)==n

        