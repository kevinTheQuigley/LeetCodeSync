# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Just need to step through the two trees identically, adding conditions for when we can't continue.
Maybe easiest to use a DFS algorithm.

for a given node, they both need the same value, and to have the same numbers of lefts/rights

'''
class Solution(object):
    def isSameTree(self, p, q):
        def dfs(p,q):
            if p is None and q is None:
                return True
            elif p is None:
                return False
            elif q is None:
                return False
            if p.val!= q.val:
                return False
            if (p.left is None and q.left is not None) or (p.left is not None and q.left is None)or (p.right is not None and q.right is None)or (p.right is not None and q.right is None):
                return False
            if p.left is not None and p.right is None:
                return dfs(p.left,q.left)
            elif q.right is not None and p.left is None:
                return dfs(p.right,q.right)
            elif p.left is not None:
                return dfs(p.right,q.right) and dfs(p.left,q.left)
            else:
                return True
        return dfs(p,q)

        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        
