class Solution(object):
    def myPow(self, x, n):
        m = 1
        if n>=0:
            if  x==-1:
                if  n%2==1:
                    m =-1
                else:
                    m=1
            else:
                while n >0:
                    m = m*x
                    n-=1
                    if m==0 or m==1:
                        break

        elif n<0:
            if x==-1:
                if  n%2==1:
                    m =-1
                else:
                    m=1
            else:
                while n<0:
                    n+=1
                    m=m/x
                    if m==0 or m ==1:
                        break

        return m
            
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
