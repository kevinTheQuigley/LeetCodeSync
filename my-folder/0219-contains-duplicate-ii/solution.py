class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        totalDict = {}
        for i in range(len(nums)):
            if nums[i] in totalDict:
                for j in totalDict[nums[i]]:
                    if abs(i-j)<=k:
                        return True
                totalDict[nums[i]] = totalDict[nums[i]] +[i]
            else:
                totalDict[nums[i]] = [i]
        return False
                
            

        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
