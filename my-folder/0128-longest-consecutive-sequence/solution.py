'''
Using sets
convert nums into a set.
pop the elements out one at a time. 
Check if the following one is present. thenn iterate down


'''

class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums)==0:
            return 0
        #nums = list(set(nums))
        numSet = set(nums)
        maxScore = 0 

        while len(numSet)>0:
            startNum = numSet.pop()
            score = 1
            nextUp = startNum+1
            while nextUp in numSet:
                numSet.remove(nextUp)
                score +=1
                nextUp +=1
            
            nextDown = startNum-1
            while nextDown in numSet:
                numSet.remove(nextDown)
                score+=1
                nextDown -=1
            maxScore = max(maxScore,score)
        return maxScore
        

        """
        :type nums: List[int]
        :rtype: int
        """
        
