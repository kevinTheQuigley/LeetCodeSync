class Solution(object):
    def isPalindrome(self, s):
        alphaString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        s = s.upper()
        n = len(s)
        j = n-1
        i = 0
        print(int(n/2))

        if n<2:
            return(True)
        while i <(n-1): 
            print(i,int(n/2)) 
    
            while s[i] not in alphaString:

                i +=1
                if i >=n-1:
                    return True                  

            print(s[i]+" is s[i]."+s[j]+" is s[j]" )  
            while s[j] not in alphaString:
                j -= 1    
            print(s[i]+" is s[i]."+s[j]+" is s[j]" )  
            if s[i] != s[j]:
                return False

            i+=1
            j-=1
        return True
        """
        :type s: str
        :rtype: bool
        """
        
