# 1290. Convert Binary Number in a Linked List to Integer
'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 45ms, Beats 98.45%
    # 17.36MB, Beats 11.91%
    def getDecimalValue(self, head: ListNode) -> int:
        temp = head
        b = ""
        
        while temp is not None:
            current_bit = temp.val
            b += str(current_bit)
            temp = temp.next

        return int(b, 2)