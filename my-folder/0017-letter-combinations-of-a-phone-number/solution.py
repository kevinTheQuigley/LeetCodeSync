class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitDict ={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        returnList = []
        def backTrack(digits,string):
            if len(digits)==0:
                return None
            digit = digits[0]
            letters = digitDict[digit]
            if len(digits[1:])==0:
                for letter in letters:
                    returnList.append(string+letter)
            else:
                for letter in letters:
                    backTrack(digits[1:],string+letter)
        backTrack(digits,"")
        return returnList


        
