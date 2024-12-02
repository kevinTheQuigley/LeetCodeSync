'''
Break it into a series of stages.
First sort the numbers.
You could then use a dfs algoirthm to search through the list, with the target being the number taken, and then checking if the other numbers are in the list.
Is there a more efficent way of doing this?

start with a target [1], remove it from the list.
iterate through the list, removing an element, adding it to a dictionary, and checking the dictionary if it's there

a,b,c,d,e
target -a, check if b,c,d,e combine to give it
target -b, check if c,d,e combine to give it....


a+b+c = 0
b+c = -c
b = -(a+c)

'''





class Solution(object):
    def threeSum(self, nums):
        distNums = nums
        returnList = []

        def findTarget(target,subList):
            numSet = set()
            
            for item in subList:
                if item in numSet:
                    sortedTriple = [target,item,-(target+item)]
                    sortedTriple.sort()
                    if not (sortedTriple in returnList):
                        returnList.append(sortedTriple)
                else:
                    numSet.add(-(target+item))
                

        for i in range(len(distNums)-1):
            target = distNums[i]
            subList = distNums[i+1:]
            findTarget(target,subList)

        return returnList
        
        


        

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
