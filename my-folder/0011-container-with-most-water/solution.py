
class Solution:
    def maxArea(self, height: List[int]) -> int:
        


        def computeArea(left: int,right: int,height)->int:
            h= min(height[left],height[right])
            area = (right-left)*h
            return area

        l = maxArea = 0
        r=len(height)-1        
        while l<r:
            area = computeArea(l,r,height)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            maxArea=max(area,maxArea)
        return maxArea
