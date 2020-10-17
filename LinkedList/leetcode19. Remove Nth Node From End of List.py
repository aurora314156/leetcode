# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast, prev = head, dummy
        for _ in range(n): 
            fast = fast.next
        while fast:
            fast = fast.next
            prev =  prev.next
        prev.next = prev.next.next
        return dummy.next