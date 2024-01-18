# 2807. Insert Greatest Common Divisors in Linked List
'''
Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 70ms, Beats 89.04%
    # 20.40MB, Beats 95.30%
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        temp = head

        if temp is None or temp.next is None:
            return head

        while temp.next is not None:
            a = temp.val
            b = temp.next.val

            n = gcd(a, b)

            new_node = ListNode(n)
            current_node = temp
            next_node = temp.next

            current_node.next = new_node
            new_node.next = next_node
            temp = next_node

        return head

