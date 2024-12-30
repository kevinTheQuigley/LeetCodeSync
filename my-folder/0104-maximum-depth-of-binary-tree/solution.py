# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Most straightforward to use a DFS call, return the max value or call the function again along both nodes
'''
class Solution(object):
    def maxDepth(self, root):
        def dfs(node,depth):
            if node is None:
                return depth
            depth+=1
            if node.left is not None or node.right is not None:
                return max(dfs(node.left,depth),dfs(node.right,depth))
            else:
                return depth
        return dfs(root,0)
            

        


            


        """
        :type root: TreeNode
        :rtype: int
        """
        
