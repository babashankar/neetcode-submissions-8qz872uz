class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(101))
        rank = [0] * 101

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])   # path compression
            return parent[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            # If both nodes share the same root → edge is redundant
            if rootA == rootB:
                return False

            # union by rank
            if rank[rootA] < rank[rootB]:
                parent[rootA] = rootB
            elif rank[rootA] > rank[rootB]:
                parent[rootB] = rootA
            else:
                parent[rootB] = rootA
                rank[rootA] += 1

            return True

        # Iterate through edges
        for a, b in edges:
            if not union(a, b):   # If union fails → redundant edge
                return [a, b]
