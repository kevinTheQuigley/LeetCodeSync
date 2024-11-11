# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):

        if head.next is None or head is None:
            return None
        
        firstPointer = head
        secondPointer = head
        iterator =0
        while firstPointer.next is not None or iterator <n :
            if firstPointer.next is None and iterator <n :
                firstPointer = head
            else:
                firstPointer = firstPointer.next
            if iterator >=n:
                secondPointer = secondPointer.next
            iterator +=1
        if secondPointer.next is not None:
            secondPointer.next = secondPointer.next.next
        else:
            head = head.next

        return head
            



        return head
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        
