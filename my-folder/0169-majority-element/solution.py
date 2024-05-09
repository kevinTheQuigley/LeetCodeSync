class Solution(object):
    def majorityElement( self, nums):
        counterList= {}
        maxi = 0
        maxiRes = 0
        for i in nums:
            if i in counterList.keys():
                counterList[i] +=1
                if counterList[i]> maxi:
                    maxi = counterList[i]
                    maxiRes= i
            else:
                counterList[i]=1
                if counterList[i]> maxi:
                    maxi = counterList[i]
                    maxiRes= i
            
        return maxiRes

