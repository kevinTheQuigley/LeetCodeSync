class Solution(object):
    def wordPattern(self, pattern, s):
        splitString = s.split(" ")
        if len (splitString)!= len(pattern):
            return False
        letterDict = {}
        wordDict = {}
        for i  in range(len(pattern)):
            letter = pattern[i]
            word = splitString[i]
            if not letter in letterDict:
                letterDict[letter] = word
            else:
                if letterDict[letter] != word:
                    return False
            if not word in wordDict:
                wordDict[word] = letter
            else:
                if wordDict[word]!= letter:
                    return False
        return True
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
