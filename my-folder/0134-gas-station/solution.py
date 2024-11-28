'''
Starting at the first station, we begin to iterate, and record the gas remaining at each station
starting at the first station
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
res  = [-2,-2,-2,3,3]
How to land on the first value?
Could try modifying the res to include what adding the list to a rotated version of the list
res1 = [-2,-2,-2,3,3]
res2 = [-2,-2,3,3,-2]
res3 = [-4,-4,1,6,1]-> Select the max from this list?


res1 = [-2,-2,-2,3,3]
using a loop with either the previous result or the current result
[-2 (or 4),-2 or -4,-2 or -4,3 or 1,3 or 6]
populates this list
[0,0,0,0,0,1] -> This includes the previous result, so 5 is the result. you go with the first value



res1 = [-1,-1,1]
     

'''

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        totalGasList = [i-j for i,j in zip(gas,cost)]
        totalGasUsed = 0
        currentGasTrip=0
        start = 0 
        for i,val in enumerate(totalGasList):
            
            totalGasUsed +=val
            currentGasTrip+=val
            if currentGasTrip <0:
                currentGasTrip =0
                start = i+1
        if totalGasUsed >=0:
            return start
        else:
            return -1
                
                


        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
