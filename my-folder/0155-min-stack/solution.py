'''
Using two indices to keep track of where the min is
Having a dict of the format {0:1,1:1,2:2} might do, where at any index, the index points to the smallest value. Could also do it like
if value1 <value2:
1:value2
if value1 get's removed, the index gets moved up
2:value2
If we add a larger value
if value3 >value2
3:value3,
no change if the  value gets removed.
what if it gets added in a different order? like
value2<value4 <value3
3 should point to value4.

What about a second list pointing to the min at all points
[1,0,4,3]

{0:0}
{0:1,1:1}
{0:1,1:1,2:2}
{0:1,1:1,2:3,2:3}



'''


class MinStack(object):

    def __init__(self):
        self.list = []
        self.minList = []
        

    def push(self, val):
        self.list.append(val)  
        if self.minList:
            if self.minList[-1] < val:
                self.minList.append(self.minList[-1])
            else:
                self.minList.append(val)
        else:
            self.minList.append(val)
        
        
        """
        :type val: int
        :rtype: None
        """
        

    def pop(self):
        if self.minList:
            self.minList.pop()
            return (self.list.pop())
        else:
            return
        
        """
        :rtype: None
        """
        

    def top(self):
        if self.list:
            return (self.list[-1])
        else:
            return
        """
        :rtype: int
        """
        

    def getMin(self):
        if self.minList:
            return self.minList[-1]
        else:
            return 
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
