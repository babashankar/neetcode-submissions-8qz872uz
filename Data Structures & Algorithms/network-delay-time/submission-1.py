class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d=[float("inf") for _ in range(n+1)]

        graph={}

        for i,j,cost in times:
            if i not in graph:
                graph[i]=[]
            if j not in graph:
                graph[j]=[]
            graph[i].append((j,cost))

        d[k]=0

        h=[(0,k)]

        while h:
            dist,node=heapq.heappop(h)

            for child,cost in graph[node]:
                tmp=dist+cost
                if tmp<d[child]:
                    d[child]=tmp
                    heapq.heappush(h,(tmp,child))
        res=max(d[1:])
        print(d)

        return res if res!=float("inf") else -1        