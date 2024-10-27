class Solution(object):
    def searchInsert(self, nums, target):
        left = 0 
        right = len(nums)-1

        while left <right:
            mid = (left+right)/2
            midValue = nums[mid]
            print(mid,left,right,midValue,target)
            if midValue <target:
                left = mid+1
            elif midValue > target:
                right = mid -1
                
            else:
                return mid
        mid = (left+right)/2
        midValue = nums[mid]
        if midValue <target or mid<0:
            mid +=1
        return mid
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
