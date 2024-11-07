
'''
We take any given point in the string and iterate out in both directions to see how long the palindrome is within the string. 
Example 
b -b also check forwards one letter to look for even palindrom
a - bab
b - aba
a -a
d -d 


'''

class Solution(object):
    def longestPalindrome(self, s):
        le = len(s)
        dp = [le*[""] for _ in range(2)]
        maxJ = 1
        if len(s)==0:
            return ""
        maxWord = s[0]
        for i in range(le):
            j = 1
            dp[0][i] = s[i]
            while (i-j)>=0 and (j+i)<=le-1:
                if(s[i-j] ==s[j+i]):
                    dp[0][i] =  s[i-j] +dp[0][i]+s[j+i]
                else:
                    break
                j = j+1
                if j*2+1 > maxJ:
                    maxJ = j*2+1
                    maxWord = dp[0][i]
                
            j = 1
            while (i-j+1)>=0 and (j+i)<=le-1:
                if (s[i-j+1] == s[i+j]):
                    dp[1][i] = s[i-j+1]+dp[1][i]+s[i+j]
                else:
                    break
                j = j+1
                if j*2 > maxJ:
                    maxJ = j*2
                    maxWord = dp[1][i]
        return maxWord    

        """
        :type s: str
        :rtype: str
        """
        
