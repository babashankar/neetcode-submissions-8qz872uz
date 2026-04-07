from collections import deque
class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        graph={i:[] for i in range(n)}
 
        indegree=[0 for _ in range(n)]
        for i,j in prerequisites:
            graph[j].append(i)
            indegree[i]+=1
        q=deque()

        for i in range(n):
            if indegree[i]==0:
                q.append(i)
        res=[]
        while q:
            node=q.popleft()

            res.append(node)
            for i in graph[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        return True if len(res)==n else False

