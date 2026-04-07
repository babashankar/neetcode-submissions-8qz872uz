import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        k=0

        d={}
        for task in tasks:
            d[task]=d.get(task,0)+1
        h=list(-1*i for i in d.values())
        heapq.heapify(h)
        q=deque()

        while h or q:
            k+=1
            if h:
                cnt=heapq.heappop(h)
                cnt+=1
                if cnt<0:
                    q.append((cnt,k+n))
            if q:
                if k==q[0][1]:
                    cnt,_=q.popleft()
                    heapq.heappush(h,cnt)
        return k

        