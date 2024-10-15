from random import choice
class RandomizedSet(object):



    def __init__(self):
        self.dict = {}


    def hasher(self,val):
        prime = 211
        l1  = prime*[None]

        total = 0 
        for val in val:
            total+=ord(val)
        total = total%prime


    def insert(self, val):
        if val not in self.dict:
            self.dict[val]=True
            return True
        else:
            return False
            

        
        """
        :type val: int
        :rtype: bool
        """
        

    def remove(self, val):
        if val in self.dict:
            self.dict.pop(val)
            return True
        else:
            return False

        """
        :type val: int
        :rtype: bool
        """
        

    def getRandom(self):
        return choice(list(self.dict.keys()))
        """
        :rtype: int
        """
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
