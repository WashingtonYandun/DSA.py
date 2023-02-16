# 21. Merge Two Sorted Lists

'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        If l1 is None, return l2. If l2 is None, return l1. If l1.val < l2.val, set temp to head to l1.val,
        and set l1 to l1.next. Otherwise, set temp to head to l2.val, and set l2 to l2.next. While l1 is not
        None and l2 is not None, if l1.val < l2.val, set temp.next to l1.val, and set l1 to l1.next.
        Otherwise, set temp.next to l2.val, and set l2 to l2.next. While l1 is not None, set temp.next to
        l1.val, set l1 to l1.next, and set temp to temp.next. While l2 is not None, set temp.next to l2.val,
        set l2 to l2.
        
        :param l1: ListNode = ListNode(1)
        :type l1: Optional[ListNode]
        :param l2: [1,2,4]
        :type l2: Optional[ListNode]
        :return: A linked list
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            temp = head = ListNode(l1.val)
            l1 = l1.next
        else:
            temp = head = ListNode(l2.val)
            l2 = l2.next

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            temp = temp.next

        while l1 is not None:
            temp.next = ListNode(l1.val)
            l1 = l1.next
            temp = temp.next

        while l2 is not None:
            temp.next = ListNode(l2.val)
            l2 = l2.next
            temp = temp.next
        return head
