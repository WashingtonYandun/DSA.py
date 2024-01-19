# 2095. Delete the Middle Node of a Linked List
'''
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # 594ms, Beats 95.70%
    # 50.36MB, Beats 99.81%
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None

        one_step = head
        two_step = head
        prev = None

        while two_step is not None and two_step.next is not None :
            prev = one_step
            one_step = one_step.next
            two_step = two_step.next.next

        prev.next = one_step.next

        return head
