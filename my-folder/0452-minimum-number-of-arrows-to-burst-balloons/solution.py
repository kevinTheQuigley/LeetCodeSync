'''
[[10,16],[2,8],[1,6],[7,12]]
Gets sorted to 
[1,6],[2,8],[7,12],[10,16]

start with 
[1,6], removes the following element,[2,8]
take the min of [6,8], iterate through the list checking if the values are contained

'''

class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key = lambda x:x[0])
        i = 0 
        while i < len(points)-1:
            if points[i][1]>=points[i+1][0]:
                points[i][1] = min(points[i+1][1],points[i][1])
                points.pop(i+1)
            else:
                i = i+1
            

        if len(points)>1:
            if points[-2][1]>points[-1][0]:
                points[-2][1] = max(points[-2][1],points[-1][1])
                points.pop(-1)
        return len(points)
            

        """
        :type points: List[List[int]]
        :rtype: int
        """
        
