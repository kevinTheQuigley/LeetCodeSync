class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_set=dict()

        for i in range(len(nums)):
            if nums[i] in num_set:
                return [i,num_set[nums[i]]]
            num_set[(target-nums[i])]=i

