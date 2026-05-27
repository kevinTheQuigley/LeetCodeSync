class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        firstPointer=head
        dummy = ListNode(next=head)

        while n>0:
            firstPointer=firstPointer.next
            n-=1
        secondPointer=dummy
        if firstPointer is None:
            print('fp is none')
        while firstPointer is not None:
            firstPointer=firstPointer.next
            secondPointer=secondPointer.next
            
        if secondPointer.next is head:
            return head.next 
        else:
            secondPointer.next = secondPointer.next.next
            return head
        
