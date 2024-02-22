# 148. Sort List
'''
Given the head of a linked list, return the list after sorting it in ascending order.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 166ms, faster than 80.32%
    # 37.33MB, less than 17.50%
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        aux = []

        while temp:
            aux.append(temp.val)
            temp = temp.next

        aux.sort()

        dummy = ListNode()
        curr = dummy

        for node in aux:
            curr.next = ListNode(node)
            curr = curr.next

        return dummy.next