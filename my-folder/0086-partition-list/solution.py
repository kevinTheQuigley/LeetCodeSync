# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        current = head
        shortListHead = None
        longListHead = shortList = longList = None
        while current is not None:
            if current.val < x:
                if shortListHead is None:
                    shortListHead = current
                    shortList = current
                else:
                    shortList.next = current
                    shortList =  shortList.next
            else:
                if longListHead is None:
                    longListHead = current
                    longList = current
                else:
                    longList.next = current
                    longList = longList.next
            current = current.next

        if shortListHead is not None:
            shortList.next = longListHead
            if longList is not None:
                longList.next = None
            return shortListHead
        else:
            if longList is None:
                return longList
            else:
                longList.next = None
                return longListHead





         
        
