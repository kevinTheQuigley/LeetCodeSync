class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        #tupleList=[(node.val,node) for node in lists]
        tupleList =[]
        i=0
        for node in lists:
            if node:
                tupleList.append((node.val,i,node))
            i+=1

        
        tupleList.sort(reverse=True)

        dummyReturn = ListNode()
        dummyNode = dummyReturn

        while len(tupleList)>0:
            dummyNode.next=tupleList.pop()[2]
            dummyNode=dummyNode.next
            if dummyNode.next:
                tupleList.append((dummyNode.next.val,i,dummyNode.next))
            tupleList.sort(reverse=True)
            i+=1
        return dummyReturn.next




