'''
The solution is built by over time checking to see if the max value is increased or decreased by adding the following values, or starting fresh from the value

Running sum for below:
[-2,1,-3,4,-1,2,1,-5,4]

[-2,1 OR -1, -3 OR -2, 4 OR -1,3 OR -1,2 or 5,1 OR 6,....]


'''

class Solution(object):
    def maxSubArray(self, nums):
        maxList = [nums[0]]
        sumTotal = nums[0]
        for num in nums[1:]:
            sumTotal = max(sumTotal+num,num)
            maxList.append(sumTotal)


        return max(maxList)

        """
        :type nums: List[int]
        :rtype: int
        """
        
