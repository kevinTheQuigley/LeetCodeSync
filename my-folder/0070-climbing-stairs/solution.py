'''
1 - 1
2 - 1+1,2
3 - 1+1+1,2+1,1+2
4 - 1+1+2,2+2,1+1+1+1,2+1+1,1+2+1


'''

class Solution(object):
    def climbStairs(self, n):
        #Calculate the number of ways, starting from 1, append it to an array, return the nth number from the array
        nthArray = []
        n=n-1
        nthArray.append(1)
        if n==0:
            return nthArray[-1]
        n=n-1
        nthArray.append(2)
        if n==0:
            return nthArray[-1]
        else:
            self._aggregateSteps(n,nthArray)
            return nthArray[-1]
        
    def _aggregateSteps(self,n,nthArray):
        
        if n<=0:
            return nthArray
        else:
            n=n-1
            nthArray.append((nthArray[-1]+nthArray[-2]))
            return self._aggregateSteps(n,nthArray)


        


    def storeValue(self,list):
        """
        :type n: int
        :rtype: int
        """
        
