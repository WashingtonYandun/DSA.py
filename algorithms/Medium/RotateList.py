# 61. Rotate List
'''
Given the head of a linked list, rotate the list to the right by k places.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 37ms, Beats 83.11%
    # 16.66MB, Beats 54.34%
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        temp =  head
        nums = []

        while temp:
            nums.append(temp.val)
            temp = temp.next

        k = k % len(nums)
        if k != 0:
            nums[:] = nums[-k:] + nums[:-k]

        dummy = ListNode()
        curr = dummy

        for i in nums:
            curr.next = ListNode(i)
            curr = curr.next

        return dummy.next