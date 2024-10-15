class Solution(object):
    def wordBreak(self, s, wordDict):
        temp = ""
        dpd = [False]*(len(s)+1)
        dpd[0] = True
        for i in range(len(s)):
            for j in range(i,len(s)):
                if dpd[i] and s[i:j+1] in wordDict:
                    dpd[j+1] = True
                    print(dpd)
        
        return dpd[-1]
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
