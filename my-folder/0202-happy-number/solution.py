''' Use a dictionary to check if it's looping. Or better yet, a set'''

class Solution(object):
    def isHappy(self, n):
        numSet = set()
        while n !=1 and not n in numSet:
            numSet.add(n)
            numList = str(n)
            temp = 0 
            for num in numList:
                temp+=int(num)*int(num)
            n = temp

        if n==1:
            return True
        else:
            return False
        """
        :type n: int
        :rtype: bool
        """
        
