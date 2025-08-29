# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        current_queue=[root]
        returnList = []
        if root is None:
            return []
        

        def findNextOrder(queue:List[TreeNode])-> List[TreeNode]:
            nextList = []
            listVals =[]
            for node in queue:
                listVals.append(node.val)
                if node.left:
                    nextList.append(node.left)
                if node.right:
                    nextList.append(node.right)
            returnList.append(listVals)
            return nextList
        while len(current_queue)>0:
            current_queue=findNextOrder(current_queue)
        
        return returnList

        
