# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev = dummy = ListNode(0)
        dummy.next = fast = head
        for _ in range(n):
            fast = fast.next
        while fast:
            fast, prev = fast.next, prev.next
        prev.next = prev.next.next
        return dummy.next