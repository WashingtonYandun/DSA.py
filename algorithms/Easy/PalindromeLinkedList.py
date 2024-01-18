# 234. Palindrome Linked List
'''
Given the head of a singly linked list, return true if it is a palindrome.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 371ms, Beats 61.92%
    # 28.24MB, Beats 53.54%
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head

        word = ""

        while temp is not None:
            word += str(temp.val)
            temp = temp.next

        if word == word[::-1]:
            return True

        return False