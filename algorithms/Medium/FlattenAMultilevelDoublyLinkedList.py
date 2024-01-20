# 430. Flatten a Multilevel Doubly Linked List
'''
You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    # 37ms, Beats 81.78%
    # 17.08MB, Beats 75.69%
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head

        while temp:
            if temp.child:
                next_node = temp.next

                temp.next = temp.child
                temp.child.prev = temp
                temp.child = None

                aux = temp.next
                while aux.next:
                    aux = aux.next

                aux.next = next_node

                if next_node:
                    next_node.prev = aux

                temp = temp.next
            else:
                temp = temp.next

        return head