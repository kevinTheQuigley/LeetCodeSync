class Solution(object):
    def hammingWeight(self, n):
        return self._calculateWeight(n,0)

    def _calculateWeight(self,n,bits):
        bitLevels = n%2
        bits+=bitLevels
        n = n//2
        if n >0:
            return self._calculateWeight(n,bits)
        else:
            return bits

        """
        :type n: int
        :rtype: int
        """
        
