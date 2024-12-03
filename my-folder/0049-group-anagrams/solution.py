'''
You could sort each one, probably the easiest one. Python allows you to compare strings.

To avoid this, I'm sure we can figure out a dictionary method. Would it look like permutations of all sorts?

I think sorting and adding to a dictionary would be the most efficient way actually lol 





'''

class Solution(object):
    def groupAnagrams(self, strs):
        anagramList = []
        returnList = []
        for st in strs:
            li = []
            for char in st:
                li.append(char)
            li.sort()
            if li in anagramList:
                returnList[anagramList.index(li)].append(st)
            else:
                anagramList.append(li)
                returnList.append([st])
        return returnList

            

        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
