'''
Using bubble sort
'''

class Solution(object):
    def findKthLargest(self, nums, k):
        return sorted(nums)[-k]
        self.kList = []
        if nums:
            self.kList.append(nums.pop())

        def bubbleSort(inputlist):
            #inputlist.sort(reverse = True)
            for j in range(len(inputlist)-1):
                j = (len(inputlist)-2)-j
                if inputlist[j] <inputlist[j+1]:
                    inputlist[j],inputlist[j+1] = inputlist[j+1],inputlist[j]
            if len(inputlist)>k:
                inputlist.pop(-1)
            return(inputlist)

        while len(nums) >0:
            num = nums.pop()
            if num > self.kList[-1] or len(self.kList)<=k:
                self.kList.append(num)
                
                bubbleSort(self.kList)
                #print(self.kList)
    
        return self.kList[-1]
                

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
