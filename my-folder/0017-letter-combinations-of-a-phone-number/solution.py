class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        letDict={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def generateLetters(inputStr,remainingDigits):
            if remainingDigits =="":
                return [inputStr]
            else:
                returnList = []
                letters = letDict[remainingDigits[0]]
                for letter in letters:
                    returnList.extend(generateLetters(inputStr+letter,remainingDigits[1:]))
                return returnList
            
        return generateLetters('',digits)

