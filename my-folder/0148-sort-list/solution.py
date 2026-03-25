
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        def splitNodeList(headNode):
            slow,fast = headNode,headNode

            while fast.next is not None and fast.next.next is not None:
                slow = slow.next
                fast = fast.next.next
            
            midNode = slow.next
            slow.next=None
            
            return midNode
        
        def joinNodeList(headNode_1,headNode_2):
            dummyNode=ListNode()
            currentNode = dummyNode

            while headNode_1 and headNode_2:
                if headNode_1.val > headNode_2.val:
                    currentNode.next = headNode_2
                    headNode_2 = headNode_2.next
                else:
                    currentNode.next = headNode_1
                    headNode_1 = headNode_1.next
                currentNode=currentNode.next
            
            if headNode_1:
                currentNode.next = headNode_1
            elif headNode_2:
                currentNode.next = headNode_2

            
            return dummyNode.next

        def mergeSort(node):
            if node and node.next:
                midNode = splitNodeList(node)
                node = mergeSort(node)
                midNode = mergeSort(midNode)
                node = joinNodeList(node,midNode)
                return node
            else:
                return node

        
        return mergeSort(head)


