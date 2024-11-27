class Solution(object):
    def reverseWords(self, s):
        word = ""
        returnString = ""
        lens = len(s)
        for i in range(lens):
            char = s[lens-1-i]
            if char ==" ":
                if word:
                    returnString+=(word)+" "
                    word = ""
            else:
                word = char+word
        
        if word:
            returnString+=(word)
        else:
            returnString = returnString[:-1]
        return returnString

            

        """
        :type s: str
        :rtype: str
        """
        
