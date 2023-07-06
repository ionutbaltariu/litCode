from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        while True:
            if not head.next:
                break
            if not head.next.next:
                head = head.next
                tmp = tmp.next
            else:
                tmp = tmp.next
                head = head.next.next

        return tmp
