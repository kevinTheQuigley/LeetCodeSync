from collections import deque
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_k(pre: ListNode, curr: Optional[ListNode], k: int) -> Optional[tuple]:
            node, count = curr, k
            while node and count > 0:          # validate k nodes exist first
                node = node.next
                count -= 1
            if count != 0:
                return None                    # fewer than k nodes remain

            stack = []
            for _ in range(k):
                stack.append(curr)
                curr = curr.next
            while stack:
                pre.next = stack.pop()
                pre = pre.next
            pre.next = curr                    # link remainder
            return (pre, curr)

        dummy = ListNode(next=head)
        result = reverse_k(dummy, head, k)
        while result:
            result = reverse_k(result[0], result[1], k)
        return dummy.next
