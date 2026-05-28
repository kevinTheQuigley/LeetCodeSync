class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummyNode = ListNode()
        headNode = dummyNode

        while  not (list1 is None or list2 is None):

            if list1.val >list2.val:
                dummyNode.next = list2
                list2=list2.next
                dummyNode=dummyNode.next
            else:
                dummyNode.next=list1
                list1=list1.next
                dummyNode=dummyNode.next

        else:
            if list1 is None:
                dummyNode.next=list2
            else:
                dummyNode.next=list1
        return headNode.next
            
