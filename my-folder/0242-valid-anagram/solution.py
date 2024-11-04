class Solution(object):
    def isAnagram(self, s, t):

        s_dict = {}
        for letter in s:
            if letter in s_dict:
                s_dict[letter]+=1
            else:
                s_dict[letter] = 1
        
        for letter in t:
            if letter in s_dict:
                s_dict[letter]-=1
            else:
                return False
        
        for letter in s_dict:
            if s_dict[letter]!=0:
                return False
        return True
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
