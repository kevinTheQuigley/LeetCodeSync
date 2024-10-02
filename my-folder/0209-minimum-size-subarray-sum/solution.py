class Solution(object):
    def minSubArrayLen(self, target, nums):
        #print(nums)
        n = len(nums)
        i = 0
        j = 0 
        sum = 0 
        minLength = n+1
        counter = 0
        tbd = False

        while i<n:
            sum +=nums[i]
            counter +=1

            if sum >=target:
                tbd = True
                while sum>=target:
                    print(i,j,counter,sum,target)
                    minLength = min(counter,minLength)
                    sum -=nums[j] 
                    counter -=1
                    j+=1
            i+=1
        

        if tbd:
            return minLength
        else:
            return 0



        

        return 0
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
