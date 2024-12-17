class Solution(object):
    def isValid(self, s):
        stack = []


        while len(s)>0:
            char = s[0]
            s = s[1:]
            if char in "([{":
                stack.append(char)
            else:
                if len(stack)==0:
                    return False
                openChar = stack.pop()
                if (char == ")" and openChar != "(") or (char == "]" and openChar != "[") or (char == "}" and openChar != "{") :
                    return False
        
        if len(stack)>0:
            return False
        
        return True
