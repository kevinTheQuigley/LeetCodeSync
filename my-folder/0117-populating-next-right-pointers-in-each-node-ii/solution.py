"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        levelList = []

        levelList.append(root)
        while len(levelList)>0:
            subList = levelList[:]
            levelList = []
            preNode = Node()
            print("starting on ",subList[0].val)
            while len(subList) >0:
                node = subList.pop(0)
                preNode.next = node
                if node.left is not None:
                    levelList.append(node.left)
                if node.right is not None:
                    levelList.append(node.right)
                preNode = node
                print(node.val)
            
        return root
                

        
