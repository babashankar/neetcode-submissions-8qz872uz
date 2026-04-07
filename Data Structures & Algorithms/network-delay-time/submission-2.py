import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        dist=[float("inf") for _ in range(n+1)]
        d={i:{} for i in range(1,n+1)}

        for i,j,m in times:
            d[i][j]=m
        print(k)
        

        dist[k]=0
        h=[(0,k)]

        while h:
            distance,node=heapq.heappop(h)

            for neig in d[node]:
                a= distance+d[node][neig]
                if a<dist[neig]:
                    dist[neig]=a
                    heapq.heappush(h,(a,neig))
        
        
        dist=dist[1:]
        return max(dist) if max(dist)!=float("inf") else -1 

        