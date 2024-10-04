class Solution(object):
    def simplifyPath(self, path):
        startList = path.split("/")
        endList = []
        if startList == []:
            return "/"
        
        for directory in startList:

            
            if directory  == "..":
                if not len(endList)==0:
                    endList.pop()
            elif (directory == "") or (directory =="."):
                None
            else:
                endList.append(directory)

        finalString = "/".join(endList)
        finalString = "/"+finalString
        return finalString


        """
        :type path: str
        :rtype: str
        """
        
