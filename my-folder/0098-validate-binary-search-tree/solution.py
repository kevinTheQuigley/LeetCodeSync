# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkNode(node,leftParent,rightParent):
            if not node:
                return True
            lowerNodes = checkNode(node.left,leftParent,node) and checkNode(node.right,node,rightParent)
            if leftParent and rightParent:
                return (leftParent.val<node.val) and (node.val<rightParent.val) and lowerNodes
            elif leftParent:
                return (leftParent.val<node.val) and lowerNodes
            elif rightParent:
                return (node.val<rightParent.val) and lowerNodes
            else:
                return lowerNodes
        
        if not root:
            return True


        return checkNode(root,None,None)
