from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d={i:[] for i in range(numCourses)}
        indegree=[0 for i in range(numCourses)]


        q=deque()
        for i,j in prerequisites:
            d[j].append(i)
            indegree[i]+=1
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        res=[]

        while q:
            node=q.popleft()
            res.append(node)

            for j in d[node]:
                indegree[j]-=1
                if indegree[j]==0:
                    q.append(j)
        return res if len(res)==numCourses else  []