class Solution(object):
    def strStr(self, haystack, needle):
        i = 0 

        while i <len(haystack):
            if haystack[i] == needle[0]:
                broken = False
                for j in range(len(needle)):
                    if i+j >len(haystack)-1:
                        return -1
                    if haystack[i+j]!= needle[j]:
                        broken = True
                        break
                if not broken:
                    return i
            i=i+1
        return -1
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
