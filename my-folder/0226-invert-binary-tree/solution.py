# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if root is None:
            return root

        def swapNodes(node):
            if (node.left is not None):
                swapNodes(node.left)
            if (node.right is not None):
                swapNodes(node.right)
            node.left,node.right =node.right,node.left
            return 
        swapNodes(root)
        return root
                
            
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        
