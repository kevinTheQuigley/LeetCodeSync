# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Find the smallest, then work upwards?
or create an index of all nodes? 

'''
class Solution(object):
    def kthSmallest(self, root, k):
        smallList = []
        def generateSmallList(node):
            if node.left is not None and len(smallList)<k:
                generateSmallList(node.left)
            if len(smallList)<k:
                smallList.append(node.val)
            if node.right is not None and len(smallList)<k:
                generateSmallList(node.right)
        
        generateSmallList(root)
        print(smallList)
        return smallList[-1]

 
            
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        
