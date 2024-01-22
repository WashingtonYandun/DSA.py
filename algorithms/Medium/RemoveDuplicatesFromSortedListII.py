# 82. Remove Duplicates from Sorted List II
'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 34ms, Beats 95.10%
    # 16.62MB, Beats 55.61%
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy

        while temp.next and temp.next.next:
            if temp.next.val == temp.next.next.val:
                k = temp.next.val
                while temp.next and temp.next.val == k:
                    temp.next = temp.next.next
            else:
                temp = temp.next

        return dummy.next