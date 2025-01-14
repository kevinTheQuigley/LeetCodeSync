'''
I wonder if we could use the values at the start and at the end?
Either way, we're going to need to pointers.
We start with pointers on either side of the list I'm guessing.
we expect the right pointer to be less then the left pointer.
we check the middle of the two pointers
4,7,2
if it's greater then the right pointer, we make our new left the right of the centerAv
if it's less then the right pointer, we make our new right to be left of the centerAv

Exit condition, left pointer is beside the right pointer
'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        i = 0
        j = len(nums)-1
        
        while j!=i+1:
            centre = int((i+j)/2)
            if nums[centre]>nums[j]:
                i = centre
            else:
                j = centre
        
        return min(nums[i],nums[j])
        
