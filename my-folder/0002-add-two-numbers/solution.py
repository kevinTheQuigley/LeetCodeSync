class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        remainder = 0
        dummyNode = ListNode()
        startNode = ListNode(next=dummyNode)

        while l1 or l2 or remainder:
            dummyNode.next = ListNode()
            dummyNode= dummyNode.next
            total = 0 
            if l1:
                total+=l1.val
                l1=l1.next

            if l2:
                total+=l2.val
                l2=l2.next

            total+=remainder

            remainder = total//10
            total = total%10

            dummyNode.val=total
        
        return startNode.next.next

