# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    [3]
[9]  -  [15,40,7]

The middle val is 3, next value popped is 9,20
[15,7] - What stops them from being popped early? If the list length is zero, they get skipped.
What if the index isn't in the list?


'''
class Solution(object):
    def buildTree(self, preorder, inorder):
        if len(preorder)==0:
            return None


        
        def takeElement(preorder,orderList):
            if orderList and preorder:
                nodeVal = preorder.pop(0) 
                node = TreeNode(val = nodeVal)
                index = orderList.index(nodeVal)

                leftList = orderList[0:index]
                rightList = orderList[index+1:]
                node.left = takeElement(preorder,leftList)
                node.right = takeElement(preorder,rightList)
                return node

        
        
        return takeElement(preorder,inorder)
        

        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        
