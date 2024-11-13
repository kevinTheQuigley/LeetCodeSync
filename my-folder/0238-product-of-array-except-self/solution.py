
'''
[1,2,3,4]

before = [1,2,6,24]

after = [24,24,12,4]

Final result = [24,12,8,6]

'''

class Solution(object):
    def productExceptSelf(self, nums):
        #Some funky pairwise multiplication? break the array down into 2, then into 2
        #Two lists, one on either side 
        nums_len = len(nums)
        numsBefore,numsAfter = [0]*nums_len,[0]*nums_len
        totalProductForward = 1
        totalProductBackward = 1
        for i in range(nums_len):
            totalProductForward = totalProductForward*nums[i]
            totalProductBackward = totalProductBackward*nums[nums_len-1-i]
            numsAfter[nums_len-1-i] = totalProductBackward
            numsBefore[i] = totalProductForward
        #print(numsBefore,"\n",numsAfter)

        for i in range(nums_len):
            if i ==0:
                nums[i] = numsAfter[1]
            elif i == nums_len-1:
                nums[i] = numsBefore[nums_len-2]
            else:
                nums[i] = numsBefore[i-1]*numsAfter[i+1]
        return nums

        

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
