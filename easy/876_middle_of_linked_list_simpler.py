from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # as long as the current node and the next one aren't None, we can allow doing .next.next since the worst case
        # is that it's None (and the condition in the while won't be respected anymore)
        tmp = head
        while head and head.next:
            tmp = tmp.next
            head = head.next.next

        return tmp
