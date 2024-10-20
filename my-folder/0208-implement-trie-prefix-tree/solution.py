class Trie(object):

    def __init__(self):
        self.mainDict = {}

        self.mainList = []

    def insert(self, word):
        idx = len(self.mainList)
        self.mainDict[word] = idx
        self.mainList.append(word)
        """
        :type word: str
        :rtype: None
        """
        

    def search(self, word):
        if word in self.mainDict.keys():
            return True
        else:
            return False
        """
        :type word: str
        :rtype: bool
        """
        

    def startsWith(self, prefix):
        charLen = len(prefix)
        for j in self.mainList:
            if j[:charLen] == prefix:
                return True
        return False


        """
        :type prefix: str
        :rtype: bool
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
