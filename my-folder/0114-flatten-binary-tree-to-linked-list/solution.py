# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
FLATTEN THE TREE
I guess there is a mapping here, but I feel like 

you could start by working your way to farthest left. 
Keep a record of the node before it.
Engange in a swap, in our instance, it's 3 and 4. 2's l points to 3. 3's right points to 4.
'''
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        stackList = []
        stackList.append(root)
        returnList  = []
        topRoot = TreeNode(val=None)
        prev = topRoot
        if root is None:
            return stackList

        while len(stackList) >0:
            current = stackList.pop()
            if current.right is not None:
                stackList.append(current.right)
            if current.left is not None:
                stackList.append(current.left)
            prev.right = current
            prev.left = None
            prev = current
        return topRoot.right



        """
        Do not return anything, modify root in-place instead.
        """
        
