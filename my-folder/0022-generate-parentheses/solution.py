class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        returnList= []

        def generateParentheses(positivity,parenthesesLeft,currentString):
            
            if positivity >0:
                # Positivity indicates the number of open parentheses already used
                # Parenthesesleft indicates the number of open parethenses not used
                generateParentheses(positivity-1,parenthesesLeft,currentString+")")
            if parenthesesLeft>0:
                generateParentheses(positivity+1,parenthesesLeft-1,currentString+"(")
            
            if positivity==0 and parenthesesLeft==0:
                returnList.append(currentString)
        
        generateParentheses(0,n,"")

        return returnList

