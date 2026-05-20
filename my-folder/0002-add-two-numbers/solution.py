class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        firstDummy=ListNode(next=dummy)
        remainder=0

        while l1 or l2 or remainder:
            dummy.next=ListNode()
            dummy=dummy.next
            total=0
            if l1:
                total+=l1.val
                l1=l1.next
            if l2:
                total+=l2.val
                l2=l2.next
            if remainder:
                total+=remainder
            
            dummy.val = total%10
            remainder = total//10
            


        return firstDummy.next.next
