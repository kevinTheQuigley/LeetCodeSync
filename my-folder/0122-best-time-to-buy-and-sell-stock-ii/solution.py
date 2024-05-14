class Solution(object):
    def maxProfit(self, prices):
        maxP = 0 
        start = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < start:
                start = prices[i]
            elif prices[i] - start> 0:
                maxP = prices[i] - start + maxP
                print(prices[i], start)
                start = prices[i]
        return maxP

        
