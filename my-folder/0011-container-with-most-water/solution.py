

'''
To calculate the volume, 
multiply the minimum height of the two pointers by the distance between them.
(i-j)*(min(nums[i],nums[j]))

Makes sense to start with the two pointers as far away as possible and iterate inwards. 
Think about a situation where you have two giant poles right in the middle.
You only need to store the max, so you don't need to use dynamic programming.
I guess you stay at the closest maximum and work inwards





'''

class Solution(object):
    def maxArea(self, height):
        i,j = 0,len(height)-1
        maxVolume = 0 
        while i!=j:
            volume = (j-i)*(min(height[i],height[j]))
            if volume >maxVolume:
                maxVolume = volume
            if height[i]>height[j]:
                j =j-1
            else:
                i = i+1
        return maxVolume

        """
        :type height: List[int]
        :rtype: int
        """
        
