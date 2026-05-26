class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letDict={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        charList=None

        while len(digits)>0:

            d=digits[0]
            digits=digits[1:]

            if charList is None:
                nextCharList=[char for char in letDict[d]]
            else:
                nextCharList=[]
                for char in charList:
                    for substring in letDict[d]:
                        nextCharList.append(char+substring)
            charList=nextCharList
        if charList is None:
            return []
        else:
            return charList

