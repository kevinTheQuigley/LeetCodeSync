# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
Some examples:-
Going all the way down to the right - fib sum - Could just work through a list of the nodes children. 

While node.left next is not none, add all children to a list, removing the previous children as you do so

'''
class Solution(object):
    def countNodes(self, root):
        startLevel = [root]

        def levelSum(nodeList,counter):
            childrenList = []
            while len(nodeList)>0:
                nextNode = nodeList.pop()
                if nextNode.left is not None:
                    childrenList.append(nextNode.left)
                if nextNode.right is not None:
                    childrenList.append(nextNode.right)
                counter +=1
            if len(childrenList)>0:
                return levelSum(childrenList,counter)
            else:
                return counter
        if root is None:
            return 0
        else:
            return levelSum(startLevel,0)
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
