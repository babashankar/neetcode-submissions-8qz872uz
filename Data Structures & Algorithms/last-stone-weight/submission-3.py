import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-i for i in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            x,y=heapq.heappop(stones),heapq.heappop(stones)
            if x==y:
                continue
            heapq.heappush(stones,-abs(x-y))
        return -stones[0] if stones else 0
        