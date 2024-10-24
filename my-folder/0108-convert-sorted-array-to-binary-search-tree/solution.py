# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):

        numLen = len(nums)
        addedCount = 0 
        left = 0
        right = numLen
        return self._addNode(nums,left,right)



    def _addNode(self,nums,left,right):
        mid = int((left+right)/2)
        nodeValue =nums[mid]
        if nodeValue is not None:
            node = TreeNode(val=nodeValue)
            nums[mid]=None
            node.left = self._addNode(nums,left,mid)
            node.right = self._addNode(nums,mid,right)
        else:
            return None
        
        return node


        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        
