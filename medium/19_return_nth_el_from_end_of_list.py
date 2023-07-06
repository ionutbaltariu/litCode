# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        element_number = 0

        head_copy = head

        while head:
            element_number += 1
            head = head.next

        head = head_copy

        how_far = element_number - n
        prev_node = None
        print(how_far)

        while head:
            print("how_far: ", how_far)
            if how_far == 0:
                print("We're in if, we are breaking after this..")
                print(head.val, prev_node, head, head.next)
                prev_node.next = head.next
                break

            prev_node = head
            head = head.next
            how_far -= 1

        return head_copy


if __name__ == "__main__":
    head = Solution().removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)

    while head:
        print(head.val)
        head=head.next
