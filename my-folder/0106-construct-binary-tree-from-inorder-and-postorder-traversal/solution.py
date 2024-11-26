# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
we now have the root nodes being the last node of the postorder list
rootValue = postorder.pop()
root = 3
then split the inorder list in two
[9],[15,20,7]

looking at the post order list again, we pop the leftmost node from postorder
node = 20
and split the inorder list similarly to above
[15],[7]
t


'''
class Solution(object):
    def buildTree(self, inorder, postorder):
        

        def appendTree(orderList,postorder):
            if orderList:
                
                nodeVal = postorder.pop()
                #print(orderList,nodeVal)
                node = TreeNode(nodeVal)
                nodeIndex = orderList.index(nodeVal)
                node.right = appendTree(orderList[nodeIndex+1:],postorder)
                node.left  = appendTree(orderList[:nodeIndex ],postorder)
                return node

        return appendTree(inorder,postorder)

        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        
