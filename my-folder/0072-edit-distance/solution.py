'''
Initial thoughts:- using a dictionary to keep track of which letters are present in each word. Not as simple, as re-arranging characters isn't a viable operation

Would it be better to do a pass over the word, looking to see which letters they have in common? I wonder if you could use two stacks. 

You could use these two temporary dictionaries, and reset them after a matching letter is found.

d1 = {inte}
d2 = {exec}
no count resets
{ntion}
{cution}

'''
class Solution(object):
    def minDistance(self, word1, word2):
        #Using the standard DP solution
        rows = len(word1) 
        cols = len(word2)

        dp = [[0 for _ in range (cols +1)] for _ in range(rows+1)]

        for i in range(1,cols+1):
            dp[0][i] = i
        for j in range(1,rows+1):
            dp[j][0] = j
        
        for j in range(1,cols+1):
            for i in range(1,rows+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1

        return dp[rows][cols]

        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
