
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_min=nums[0]
        total_max=nums[0]
        local_max=nums[0]
        local_min=nums[0]
        total_sum=nums[0]

        for i in range(1,len(nums)):
            local_max=max(nums[i],nums[i]+local_max)
            total_max=max(total_max,local_max)

            local_min=min(nums[i],nums[i]+local_min)
            total_min=min(local_min,total_min)

            total_sum+=nums[i]
            print(local_max,local_min,total_max,total_min,total_sum)

        circular_sum = total_sum-total_min

        if circular_sum==0:
            return total_max

        return max(total_max,circular_sum) 
