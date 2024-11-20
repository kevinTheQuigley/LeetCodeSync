'''
intervals are now sorted by the first number:-

We start with the first entry, if the second value of the entry is less then the first of the next, join them, else move onto the next entry

'''
class Solution(object):
    def merge(self, intervals):
        intervals.sort(key = lambda x:x[0])
        returnIntervals = []

        while len(intervals)>0:
            interval = intervals.pop(0)
            while len(intervals)>0:
                intervalTemp = intervals[0]
                if intervalTemp[0]<=interval[1]:
                    interval[1] = max(interval[1],intervalTemp[1])
                    intervals.pop(0)
                else:
                    break
            returnIntervals.append(interval)
        return returnIntervals



        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
