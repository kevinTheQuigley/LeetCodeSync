# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        self.levelAverages = []
        self.levelList = []
        self.levelList.append(root)
        while len(self.levelList)>0: 

            newList = []
            len1 = len(self.levelList)
            levelAverage = 0
            for i in range(len1):
                node = self.levelList.pop()
                levelAverage += node.val
                if node.left is not None:
                    newList.append(node.left)
                if node.right is not None:
                    newList.append(node.right)
            levelAverage = float(levelAverage)/len1
            self.levelAverages.append(levelAverage)
            self.levelList = newList
        return self.levelAverages

        


        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        
