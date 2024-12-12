"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

Going to iterate over two steps; one to generate the copied list.


"""

class Solution(object):
    def copyRandomList(self, head):
        if head is None:
            return None

        headCopy = Node(head.val)
        copyNode = headCopy
        mainNode = head
        randomDict = {}
        copyNodeList = [headCopy]
        mainNodeList = [head]

        while mainNode.next is not None:
            mainNode = mainNode.next
            copyNode.next = Node(mainNode.val)
            copyNode = copyNode.next

            copyNodeList.append(copyNode)
            mainNodeList.append(mainNode)
            
            
        
        mainNode = head
        copyNode = headCopy

        while mainNode is not None:
            randNode = mainNode.random
            if randNode is not None:
                ind = mainNodeList.index(randNode)
                copyNode.random = copyNodeList[ind]
            else:
                copyNode.random = None
            copyNode = copyNode.next
            mainNode = mainNode.next

        return headCopy
        



        
