class Solution(object):
    def removeDuplicates(self,nums):
        i = 0 
        while i < (len(nums)-2):
            if nums[i]==nums[i+1]:
                nums[i:]=nums[i+1:]
                print(nums[i])
                print(nums[i+1])
            else:
                i+=1
        k = len(nums)
        if(1<len(nums)):
            if(nums[-1]==nums[-2]):
                k=k-1 
                nums=nums[:-1]
        return(k) 
        """
        :type nums: List[int]
        :rtype: int
        """
            
