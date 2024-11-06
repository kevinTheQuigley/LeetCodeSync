'''
Walking throught the base example

starts with negative inf (Smallest value possible). We start with the root. (7),
we then go down, and two the left. There are no children, so we go up and to the right. How do we map this, when the relationship is just between parents to children and doesn't go back up?

If we start at the root, we go down as far as possible to the left. I think this could be stored as a dictionary. Let's discuss:

currentNode is either in leftDict or rightDict. if we go down one node to the left, we append it to leftDict, with the key being the child, the parent being the other key.
Then we know the next node is the parent node.
If we go to the right, we append it to rightDict. every right dict parent should have a leftDict parent eventually. we just need to reuse them.

Suppose we have an extra couple of digits in the current example, 1 and 5

                7
               /  \
            3       15
           / \       / \
          1   5     9   20

while left child is not none:
    leftDict = {3:7,1:3}
    After going up
    leftDict = {3:7}
    if rightChild is not None....
    rightDict = {5:3}
    if child in rightDict,while node is in the right dict got up from right child, and one left. 
    Need to save the root node as a special value, that gets checked when moving up from the right, as it's a special condition.



'''



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator(object):

    def __init__(self, root):
        self.leftDict = {}
        self.rightDict = {}
        self.root = root
        self.currentNode = root
        while self.currentNode.left is not None:
            self.leftDict[self.currentNode.left] = self.currentNode
            self.currentNode = self.currentNode.left
        lastNode = TreeNode(val = self.currentNode.val -1)

        self.currentNode.left = lastNode
        self.leftDict[lastNode] = self.currentNode
        self.currentNode = lastNode


        """
        :type root: Optional[TreeNode]
        """
        

    def next(self):
        if self.currentNode in self.leftDict and self.currentNode.right is None:
            self.currentNode = self.leftDict[self.currentNode]
            return self.currentNode.val
        elif not self.currentNode.right is None:
            self.rightDict[self.currentNode.right] = self.currentNode
            self.currentNode = self.currentNode.right
            while self.currentNode.left is not None:
                self.leftDict[self.currentNode.left] = self.currentNode
                self.currentNode = self.currentNode.left
            return self.currentNode.val
        elif self.currentNode in self.rightDict:
            while self.currentNode in self.rightDict:
                self.currentNode = self.rightDict[self.currentNode]
                if self.currentNode == self.root:
                    return False
            if self.currentNode in self.leftDict:
                self.currentNode  = self.leftDict[self.currentNode]
            return self.currentNode.val
            
        """
        :rtype: int
        """
        

    def hasNext(self):

        if self.currentNode in self.rightDict and self.currentNode.right is None:
            checkNode = self.currentNode
            while checkNode in self.rightDict:
                checkNode = self.rightDict[checkNode]
                if checkNode == self.root:
                    return False
        elif self.currentNode == self.root and self.currentNode.right is None:
            return False
        return True
            

            
        """
        :rtype: bool
        """
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
