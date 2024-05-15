class Solution(object):
    def canJump(self, nums):
        jump = nums[0]
        li = len(nums)
        i = 1
        while  jump >=0:
            #print(i,jump,li)
            if i >= li:
                return True
            if jump < nums[i-1]:
                jump = nums[i-1]
            jump-=1
            i+=1
        return False
