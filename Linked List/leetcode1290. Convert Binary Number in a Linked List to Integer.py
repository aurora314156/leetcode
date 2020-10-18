# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        prev = None
        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current
        ans, pos = 0, 1
        head = prev
        while head:
            ans += head.val * pos 
            head = head.next
            pos *= 2
        return ans
            