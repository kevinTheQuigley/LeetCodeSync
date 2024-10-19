# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def getList(self,current,orderedList):
        if current.left is not None:
            self.getList(current.left,orderedList)
        orderedList.append(current.val)
        if current.right is not None:
            self.getList(current.right,orderedList)


    def getMinimumDifference(self, root):
        if root is None:
            return 0

        orderedList = []
        self.getList(root, orderedList)
        print(orderedList)
        minVal = orderedList[1]- orderedList[0]
        for i in range(len(orderedList)-1):
            minVal = min((orderedList[i+1]-orderedList[i]),minVal)
        return minVal


        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
