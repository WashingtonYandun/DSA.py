# 1019. Next Greater Node In Linked List
'''
You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 164ms, Beats 87.10%
    # 20.45MB, Beats 84.76%
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        result = []
        index = 0
        
        current = head

        while current:
            result.append(0)

            while stack and stack[-1][0] < current.val:
                _, i = stack.pop()
                result[i] = current.val

            stack.append((current.val, index))
            index += 1
            current = current.next

        return resul