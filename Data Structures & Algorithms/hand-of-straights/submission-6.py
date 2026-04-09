import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        l=len(hand)
        if l%groupSize!=0:
            return False
        d={}
        for i in hand:
            d[i]=d.get(i,0)+1
        heap=list(d.keys())
        heapq.heapify(heap)
        print(d)
        

        while heap:
            if d[heap[0]]==0:
                heapq.heappop(heap)
                continue
            start=heap[0]
            i=0
            while i<groupSize:
                if start+i in d and d[start+i]>0:
                    d[start+i]-=1
                    i+=1
                else:
                    return False

        return True
            

        
        