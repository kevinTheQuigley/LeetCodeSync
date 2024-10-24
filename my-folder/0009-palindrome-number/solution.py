class Solution(object):
    def isPalindrome(self, x):
        numList = []
        if x<0:
            return False
        while x >0:
            numList.append(x%10)
            x = x//10
        length = len(numList)
        for i in range((length/2)):
            if numList[i] !=numList[-i-1]:
                return False
        return True
        """
        :type x: int
        :rtype: bool
        """
        
