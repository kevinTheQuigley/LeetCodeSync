class Solution:
    def isValid(self, s: str) -> bool:
        parenStack = list()
        parenDict={
            "{":"}",
            "[":"]",
            "(":")"
        }

        while len(s)>0:
            p=s[0]
            s=s[1:]
            if p in "{[(":
                parenStack.append(parenDict[p])
            else:
                if len(parenStack)==0:
                    return False
                char = parenStack.pop()
                if char !=p:
                    return False
        if len(parenStack)==0:
            return True
        else:
            return False
        
        
