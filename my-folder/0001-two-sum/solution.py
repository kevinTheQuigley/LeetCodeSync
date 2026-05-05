
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetDict : dict = dict()

        for i in range(len(nums)):
            if nums[i] in targetDict:
                return(i,targetDict[nums[i]])
            else:
                targetDict[target-nums[i]]=i


