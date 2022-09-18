# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        idx = 1
        number_one = number_two = 0

        while l1 is not None:
            number_one += l1.val * idx
            l1 = l1.next
            idx *= 10

        idx = 1
        while l2 is not None:
            number_two += l2.val * idx
            l2 = l2.next
            idx *= 10

        s = number_one + number_two
        head = ListNode(s % 10)
        head_cpy = head
        s //= 10

        while s != 0:
            head.next = ListNode(s % 10)
            head = head.next
            s //= 10

        return head_cpy


if __name__ == "__main__":
    n1 = ListNode(2)
    n2 = ListNode(4)
    n3 = ListNode(3)
    n4 = ListNode(5)
    n5 = ListNode(6)
    n6 = ListNode(4)

    n1.next = n2
    n2.next = n3

    n4.next = n5
    n5.next = n6

    returned_head = Solution().addTwoNumbers(n1, n4)
    while returned_head:
        print(returned_head.val, end='')
        returned_head = returned_head.next
