#class Solution(object):
#    def rotate(self, nums, k):
#        lh= len(nums)
#        ls = []
#        for i in range(lh):
#            ls.append(nums[(i+k+1)%lh])
#        nums = ls
#        return nums

class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        a=k%len(nums)
        nums[:]=nums[-a:]+nums[:-a]
        return nums
