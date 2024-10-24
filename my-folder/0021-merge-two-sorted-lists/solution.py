# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        returnNode = ListNode()
        firstNode = returnNode

        while list1 is not None or list2 is not None:
            if list1 is not None and list2 is None:
                returnNode.next = ListNode(list1.val)
                returnNode = returnNode.next
                list1 = list1.next
            elif list1 is None and list2 is not None:
                returnNode.next = ListNode(list2.val)
                returnNode = returnNode.next
                list2 = list2.next
            else:
                if list1.val>list2.val:
                    returnNode.next = ListNode(list2.val)
                    returnNode = returnNode.next
                    list2 = list2.next
                else:
                    returnNode.next = ListNode(list1.val)
                    returnNode = returnNode.next
                    list1 = list1.next
        return firstNode.next
            
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
