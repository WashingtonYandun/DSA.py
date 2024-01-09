# 2. Add Two Numbers
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # A extremely bad solution... I will improve it

    # 93 ms, faster than 5.73%
    # 16.4 MB, less than 29.50%
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []

        aux1 = l1
        aux2 = l2

        while aux1:
            num1.append(str(aux1.val))
            aux1 = aux1.next

        while aux2:
            num2.append(str(aux2.val))
            aux2 = aux2.next

        total = int("".join(num1[::-1])) + int("".join(num2[::-1]))
        total_str = str(total)[::-1]

        dummy = ListNode()
        curr = dummy

        for digit in total_str:
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy.next      