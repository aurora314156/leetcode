# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lstart = less = ListNode(0)
        gstart = greater = ListNode(0)
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            elif head.val >= x:
                greater.next = head
                greater = greater.next
            head = head.next
        greater.next = None
        less.next = gstart.next
        return lstart.next