'''
You could split the intervals into starts and ends, and create two sets to find out if lower or highter values are present?
Could you figure out the new index of your new interval when it get's added?
Could you use some kind of binary search?

'''

class Solution(object):
    def insert(self, intervals, newInterval):
        if len(intervals)==0:
            intervals.append(newInterval)
            return intervals

        i = 0 
        while i<len(intervals):
            if intervals[i][0]<=newInterval[0]:
                i = i+1
            else:
                break

        if i!=0:
            if intervals[i-1][1]>=newInterval[0]:
                print(max(newInterval[1],intervals[i-1][1]))
                intervals[i-1][1] = max(newInterval[1],intervals[i-1][1])
                i = i-1
            else:
                intervals.insert(i,newInterval)
        else:
            intervals.insert(i,newInterval)


        while i+1 <len(intervals):
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i+1)
            else:
                break
        return intervals
        
        
        

        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
