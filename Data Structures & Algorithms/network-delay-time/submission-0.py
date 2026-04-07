import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        h=[]
        heapq.heappush(h,(0,k-1))
        dist=[float("inf") for _ in range(n)]
        dist[k-1]=0

        adj={i:[] for i in range(n)}
        for i,j,we in times:
            adj[i-1].append((j-1,we))
       
        while h:
            cost,node=heapq.heappop(h)
            for nei,we in adj[node]:
                tmp=cost+we
                if cost+we<dist[nei]:
                    dist[nei]=cost+we
                    heapq.heappush(h,(cost+we,nei))
        m=max(dist)
        return m if m!=float("inf") else -1
        
        
        
            



        