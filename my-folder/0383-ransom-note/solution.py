class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        alphabet_hash = 26*[0]
        alphabet_string = "abcdefghijklmnopqrstuvwxyz"
        for letter in magazine:
            temp = alphabet_string.index(letter)
            alphabet_hash[temp]+=1
        
        for letter in ransomNote:
            temp = alphabet_string.index(letter)
            alphabet_hash[temp]-=1
        
        for i in alphabet_hash:
            if i<0:
                return False
        return True
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
