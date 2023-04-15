# 234. Palindrome Linked List
'''
Given the head of a singly linked list, return true if it is a palindrome.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 1059 ms, faster than 43.87%
    # 44.6 MB, less than 65.43%
    # must be improved => Could i do it in O(n) time and O(1) space?
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        initialState = []
        reversedState = []
        aux = head
        while aux is not None:
            initialState.append(str(aux.val))
            aux = aux.next

        current = head
        prev = None

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev

        aux = head
        while aux is not None:
            reversedState.append(str(aux.val))
            aux = aux.next

        if initialState == reversedState:
            return True

        return False
