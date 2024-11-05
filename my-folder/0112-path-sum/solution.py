# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):

        

        def dfs(node,targetSum,currentSum):
            leftVal = False
            rightVal = False

            currentSum += node.val
            if node.left is not None or node.right is not None:
                if node.left is not None:
                    leftVal = dfs(node.left,targetSum,currentSum)
                if node.right is not None:
                    rightVal = dfs(node.right,targetSum,currentSum)
                return leftVal+rightVal
            else:
                if targetSum == currentSum:
                    return True
                else:
                    return False
        
        if root is not None:
            return  [True if dfs(root,targetSum,0) else False][0]
        else:
            return False
            
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        
