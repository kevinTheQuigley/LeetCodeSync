class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs)<1:
            return ""
        elif len(strs)==1:
            prefix = strs[0]
            return prefix

        prefix = strs[0]
        le = len(prefix)
        for word in strs:
            if len(word)<prefix:
                prefix = prefix[:len(word)]
                le = len(prefix)
            for i in range(le):
                
                if not prefix[i]==word[i]:
                    prefix = prefix[:i]
                    le = len(prefix)

                    break
            if le ==0:
                break
        return prefix


        """
        :type strs: List[str]
        :rtype: str
        """
        
