class Solution(object):
    def maxProfit(self, prices):
        maxP = 0 
        start = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < start:
                start = prices[i]
            elif prices[i] - start> maxP:
                maxP = prices[i] - start
        return maxP


        """
        :type prices: List[int]
        :rtype: int
        """
