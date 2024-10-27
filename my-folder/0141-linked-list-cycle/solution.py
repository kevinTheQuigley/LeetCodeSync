# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        #I wonder if we could use a dictionary?
        bigDict = {}
        node = head
        returnVal = False
        if node ==None:
            return False
        while node.next is not None:
            if (node in bigDict):
                returnVal = True
                break
                

            bigDict[node] = node.val
            node = node.next
        return returnVal

        """
        :type head: ListNode
        :rtype: bool
        """
        
