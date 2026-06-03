
class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        maxPalinDrome=""

        def findPalinDrome(i,j):
            
            while i>=0 and j< len_s and s[i]==s[j]:
                i-=1
                j+=1
            return s[i+1:j]

        for i in range(len_s):
            odd_palinDrome=findPalinDrome(i,i)
            even_palinDrome=findPalinDrome(i,i+1)

            if len(odd_palinDrome)>len(maxPalinDrome):
                maxPalinDrome=odd_palinDrome
            if len(even_palinDrome)>len(maxPalinDrome):
                maxPalinDrome=even_palinDrome

        
        return maxPalinDrome







