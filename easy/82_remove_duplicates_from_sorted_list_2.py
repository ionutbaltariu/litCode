from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head

        if not head or head.next is None:
            return head
        anterior = None
        while tmp.next is not None:
            if tmp.val == tmp.next.val:
                while tmp.next is not None and tmp.val == tmp.next.val:
                    tmp.next = tmp.next.next
                print('###', tmp.val)
                if not anterior and tmp.next:
                    tmp = tmp.next

                if anterior and tmp.next:
                    anterior.next = tmp.next
            else:
                anterior = tmp
                tmp = tmp.next
        return head


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
    h = Solution().deleteDuplicates(head)
    while h:
        print(h.val)
        h = h.next

