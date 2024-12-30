# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
Let's think about movement conditions:
First, if back node is at the head, and skipping is true, move the head to the new point;

Choice is simple, are we moving the backNode.next to skip the value?
if front = front.next:
    skipNode =True
    frontNode= front.next.next
if skipNode:
    backNode.next = front.next.next



'''
class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        back=head
        front = head
        skipVal = False
        atHead =True

        while front is not None:
            if front.next is None:
                return head
            if front.val ==front.next.val:
                skipVal =True
                while front.val ==front.next.val:
                    
                    front = front.next
                    if front.next is None:
                        break
                front=front.next

                if atHead:
                    head = front
                    back =head
                else:
                    back.next =front
            else:
                atHead =False
                back = front
                front = front.next
        return head

            


        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
