# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Need to start with catching the pre node, then appending the nodes to a stack, then popping them off to re-orient them

'''


class Solution(object):
    def reverseBetween(self, head, left, right):
        currentNode = head
        preNode = currentNode
        nodeStack = []
        flipHead = False
        if 1 == left:
            flipHead = True
        i =1
        while i != left and currentNode.next is not None:
            preNode = currentNode
            currentNode = currentNode.next
            i+=1
            
        
        while i!=right :
            i+=1
            nodeStack.append(currentNode)
            if currentNode.next is None:
                break
            currentNode = currentNode.next 

            
        


        
        
        lastNode = currentNode.next

        
        if flipHead:
            head=currentNode
        else:
            preNode.next = currentNode

        priorNode = currentNode
        print(len(nodeStack))

        while len(nodeStack)>0:
            currentNode = nodeStack.pop()
            priorNode.next = currentNode
            priorNode = currentNode
        
        currentNode.next = lastNode
        return head
        
        
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        
