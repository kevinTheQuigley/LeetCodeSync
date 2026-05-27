

class Solution:
    def reverse(self, x: int) -> int:

        rev=0
        upper=(2**31)-1
        lower=2**31

        if x<0:
            bound = lower
            isNeg=True
            x*=-1
        else:
            isNeg=False
            bound=upper
        
         
        while 0<x<bound:
            rev*=10
            rev+=x%10
            x//=10

        if rev>bound:
            return 0
        
        if isNeg:
            return -rev
        else:
            return rev

