'''
Treat the numbers as elements to add to the queue
pop off the first, add it to our "numbers stack".
Keep going until you come across something that's not a number.
Order of operations matters for division and multiplication. First number popped is on the right hand side of the equation.
check if isnumeric

While len(tokens)>0:
    pop element off the starting list(), append it to a queue. 

'''

class Solution(object):
    def evalRPN(self, tokens):
        numberStack = []
        if len(tokens)<2:
            return int(tokens[0])
        while len(tokens)>0:
            item = tokens.pop(0)
            if ord(item[-1])>47 and ord(item[-1])<58:
                numberStack.append(item)
            else:
                
                rightNumber = int(numberStack.pop())
                leftNumber = int(numberStack.pop())
                if item == '+':
                    latestNum = leftNumber + rightNumber
                elif item == '-':
                    latestNum = leftNumber - rightNumber
                elif item == '*':
                    latestNum = leftNumber * rightNumber
                elif item == '/':
                    # Perform integer division (truncate towards zero)
                    latestNum = int(leftNumber / float(rightNumber))
                
                numberStack.append(str(latestNum))
        return latestNum




        """
        :type tokens: List[str]
        :rtype: int
        """
        
