"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list."""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = start_of_res = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                res.next = list1
                list1, res  = list1.next, list1
            else:
                res.next = list2
                list2, res = list2.next, list2

        if list1 or list2:
            res.next = list1 if list1 else list2

        return start_of_res.next


s = Solution()
print(s.mergeTwoLists(list1=[1, 2, 4], list2=[1, 3, 4]))
print(s.mergeTwoLists(list1=[], list2=[]))
print(s.mergeTwoLists(list1=[], list2=[0]))
print(s.mergeTwoLists(list1=[11, 12, 24], list2=[11, 13, 14]))
