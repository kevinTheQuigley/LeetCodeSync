# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level = [root]
        return_queue = []

        def checkLevel():
            nonlocal level
            nextLevel = []
            lastNode = None
            while len(level)>0:
                node = level.pop(0)
                if node is not None:
                    lastNode = node
                    nextLevel.append(node.left)
                    nextLevel.append(node.right)
            level = nextLevel
            if lastNode is not None:
                return_queue.append(lastNode.val)
                
        while len(level)>0:
            checkLevel()
        
        return return_queue


        

