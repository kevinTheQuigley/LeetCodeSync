'''
1 2 3 4 5

rotated by 2
4 5 1 2 3

using two pointers, seperated by two, and stopping when the second gets to the end

1 2 3 4 5
    ^   ^
take 5 point it to head

1 2 3 4 5 1 2 3 ...
take what three points too, and make that head
4 5 1 2 3 4 5 ....

and make three point to none....
4 5 1 2 3


counter goes 
1,2

at 1, counter is 1, self.next is not none
at 2, counter is 2, self.next is None, counter is reset for the next one
back at 1, counter is 1




1,2

'''



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head is None or head.next is None:
            return head
        firstPointer = head
        counter =0
        while counter <k:
            #print(counter,k)
            if firstPointer.next is None:
                k = k%(counter+1)
                counter = 0
                firstPointer = head
            else:
                firstPointer = firstPointer.next
                counter+=1
            

            


            
        
        secondPointer = head
        while firstPointer.next is not None:
            firstPointer = firstPointer.next
            secondPointer = secondPointer.next

        firstPointer.next = head
        head = secondPointer.next
        secondPointer.next = None
        return head



        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        
