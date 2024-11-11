'''
Using some kind of DFS algorithm.
Used this before to generate every kind of combination, but how to keep track of which numbers have been used before?
Use a dictionary?


[1,2,3,4]

1
[2,3,4]

2 
[3,4]

3
[4]





'''
class Solution(object):
    def combine(self, n, k):
        numList = range(1,n+1)

        def dfs(level,outputList,num,inputList):
            #print(num)
            level -=1
            outputList = outputList[:]
            outputList.append(num)
            if level ==0:

                return [outputList]
            else:
                totalOutputList = []
                newInputList = inputList[:]
                while len(newInputList)>=level:
                    inputNumber = newInputList.pop(0)
                    totalOutputList.extend(dfs(level,outputList,inputNumber,newInputList))
                return totalOutputList
        returnList = []
        while len(numList)>=k:
            num = numList.pop(0)
            returnList += dfs(k,[],num,numList)

        return returnList



        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
