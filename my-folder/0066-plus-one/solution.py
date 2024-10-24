class Solution(object):
    def plusOne(self, digits):
        digitString = "".join(str(digit)for digit in digits)
        digitInt = int(digitString)
        digitInt +=1
        digitString = str(digitInt)
        returnStringDigits = (list(digitString))
        print(digitString,digitInt,returnStringDigits)
        returnInts = [int(digit) for digit in returnStringDigits]
        return returnInts
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
