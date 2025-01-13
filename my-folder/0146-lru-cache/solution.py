'''
Maintain a set of what is/isn't present.
Could use a deque to add/remove items. Need to iterate through it. 
'''

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.s = dict()
        self.l = []
        

    def get(self, key: int) -> int:
        if key in self.s:
            val = self.s[key]
            self.l.remove(key)
            self.l = [key]+self.l
            
            return val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.s:
            self.s[key]=value
            self.l = [key]+self.l
            if len(self.l)>self.capacity:
                rk = self.l.pop()
                self.s.pop(rk)
        else:
            self.s[key]=value
            self.l.remove(key)
            self.l = [key]+self.l

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
