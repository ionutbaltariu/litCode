# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # solution with a dummy node and another ptr that follows the next element (the one that should be put in the merged list (the smallest))
        # same idea as mege of two arrays but easier since we can just use 'next' references in order to paste the whole remaining list (which can be either list1 or list2)
        merged_head = ListNode()
        follower = merged_head

        while list1 and list2:
            if list1.val < list2.val:
                follower.next = list1
                list1 = list1.next
            else:
                follower.next = list2
                list2 = list2.next

            # we just advance the following pointer to the next position
            follower = follower.next

        # remaining elements from one of the lists

        if list1:
            follower.next = list1

        if list2:
            follower.next = list2

        return merged_head.next
