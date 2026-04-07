import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d={}

        for i in hand:
            d[i]=d.get(i,0)+1
        vals=list(d.keys())
        heapq.heapify(vals)

        while vals:
            mini=vals[0]
            if mini in d and d[mini]>0:
                t=0
                while t<groupSize and mini+t in d:
                    d[mini+t]-=1
                    if d[mini+t]==0:
                        del d[mini+t]
                    t+=1
                if t<groupSize:
                    return False

            else:
                heapq.heappop(vals)
        return True if not d else False

        
        