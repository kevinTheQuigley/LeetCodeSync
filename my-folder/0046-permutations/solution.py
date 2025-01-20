class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        returnList=[]

        def backtrack(outputList,inputList):
            if len(inputList)==0:
                returnList.append(outputList)
            for i in range(len(inputList)):
                inputChar= inputList[i]
                backtrack(outputList+[inputChar],inputList[:i]+inputList[i+1:])

        backtrack([],nums)
        return returnList
        
