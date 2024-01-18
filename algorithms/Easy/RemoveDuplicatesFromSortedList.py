# 83. Remove Duplicates from Sorted List
'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 31ms, Beats 98.34%
    # 17.44MB, Beats 5.97%
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head

        while temp is not None and temp.next is not None:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return head