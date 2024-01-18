# 876. Middle of the Linked List
'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 24ms Beats, 99.16%
    # 17.14Mb Beats, 46.93%
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        one_step = head
        two_step = head

        while two_step is not None and two_step.next is not None :
            one_step = one_step.next
            two_step = two_step.next.next

        return one_step
            