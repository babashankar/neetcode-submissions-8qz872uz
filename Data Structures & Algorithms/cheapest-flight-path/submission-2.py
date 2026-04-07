class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d={i:[] for i in range(n)}

        for i,j,cost in flights:
            d[i].append((j,cost))
        def dfs(src,dst,n):
            if n < -1:
                return float("inf")
            if src==dst:
                return 0
            c=float("inf")
            for i,cost in d[src]:
                print(src,"->",i,n)
                c=min(c,cost+dfs(i,dst,n-1))
            return c
        a=dfs(src,dst,k)
        return a if a!=float("inf") else -1















        