from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        have_cycle = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                have_cycle = True
                break

        # after we found a cycle, we move the fast pointer back to the head
        # and then just move it one step at a time
        # until it reaches the 'slow' pointer
        # that should be the beginning of the list
        if have_cycle:
            fast = head
            while slow != fast:
                slow = slow.next
                fast = fast.next

            return fast
        else:
            return None