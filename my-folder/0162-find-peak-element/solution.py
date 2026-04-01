class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums_len= len(nums)
        left = 0
        right=nums_len-1
        if right ==0:
            return left

        while left !=right:
            mid=(left+right)//2
            mid_p1=mid+1
            if nums[mid]>nums[mid+1]:
                right = mid
            else:
                left = mid+1

        mid=(left+right)//2
        mid_p1=mid+1
        return mid
