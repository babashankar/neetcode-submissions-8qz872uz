class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        mini=prices[0]
        res=0

        for i in range(1,len(prices)):
            if prices[i]>mini:
                res=max(res,prices[i]-mini)
            else:
                mini=prices[i]
        return res
        