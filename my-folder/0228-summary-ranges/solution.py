class Solution(object):
    def summaryRanges(self, nums):
        top = 0
        onBottom = False
        i = 0 
        rangeArray = []
        if nums ==[]:
            return []
        bottom = nums[0]
        start = nums[0]
        end = nums[-1]
        number = start

        for i in range(len(nums)-1):
            if nums[i]+1 == (nums[i+1]):
                if not onBottom:
                    bottom = nums[i]
                onBottom = True
            else:
                top = nums[i]
                onBottom = False
                
                if top ==bottom:
                    rangeArray.append(str(top))
                else:
                    rangeArray.append(str(bottom)+"->"+str(top))
                bottom = nums[i+1]

        top = nums[-1]
        if onBottom:
            if top ==bottom:
                rangeArray.append(str(top))
            else:
                rangeArray.append(str(bottom)+"->"+str(top))
        else:
            rangeArray.append(str(top))

            



        return rangeArray



        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
