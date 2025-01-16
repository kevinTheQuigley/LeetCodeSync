'''
So here we can use a backtracking recursive solution.
We need to keep track of two stacks, the left braces and the right braces.
We can't use a right brace before using a left brace. How should we keep track of this? I think we should only add to the list of right brackets after addingto the left.
So you pop one off the leftStack. Then you can call the function again


'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        leftStack = n*"("
        rightStack = ""
        returnList = []

        def dfs(leftS:str,rightS:str,currentS):

            if len(leftS)==0 and len(rightS)==0:
                returnList.append(currentS)
            else:
                if len(leftS) >0:
                    dfs(leftS[1:],rightS+")",currentS+leftS[0])
                if len(rightS)>0:
                    dfs(leftS,rightS[1:],currentS+rightS[0])
        
        dfs(leftStack,rightStack,"")
        return returnList

        
