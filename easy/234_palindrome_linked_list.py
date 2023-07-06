from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        digits = deque()
        copy = head

        if not head.next:
            return True

        while head:
            digits.append(head.val)
            head = head.next

        # slow is the middle
        while digits and copy:
            if digits.pop() != copy.val:
                return False
            copy = copy.next

        if digits or copy:
            return False

        return True
