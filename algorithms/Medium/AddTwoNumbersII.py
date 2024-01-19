# 445. Add Two Numbers II
'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 57ms, Beats 80.70%
    # 17.49MB, Beats 14.85%
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = l1
        n1 = ""

        while temp:
            n1 += str(temp.val)
            temp = temp.next
        
        temp = l2
        n2 = ""

        while temp:
            n2 += str(temp.val)
            temp = temp.next

        addition = [int(i) for i in str(int(n1) + int(n2))]

        dummy = ListNode()
        curr = dummy

        for i in addition:
            curr.next = ListNode(i)
            curr = curr.next

        return dummy.next