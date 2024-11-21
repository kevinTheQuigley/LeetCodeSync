# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
generate two stacks of all elements, compare each element until there isn't any more to compare


'''
class Solution(object):
    def isSymmetric(self, root):
        if root.left is None:
            if root.right is not None:
                return False
            else:
                return True
        leftNode = root.left
        leftList = [leftNode]
        rightNode = root.right
        rightList = [rightNode]
        def dfs(rightNode,leftNode):
            if (leftNode is None or rightNode is None) and leftNode is not rightNode:
                return False
            elif leftNode is None and rightNode is None:
                return True
            elif leftNode.val != rightNode.val:
                return False
            else:
                return (dfs(rightNode.right,leftNode.left)and dfs(rightNode.left,leftNode.right))

        return dfs(rightNode,leftNode)
            
            
                
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
