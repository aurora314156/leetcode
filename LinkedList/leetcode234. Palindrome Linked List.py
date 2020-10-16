# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head
        if not slow and not fast: return True
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        n_head = slow
        prev = None
        while n_head:
            current = n_head
            n_head = n_head.next
            current.next = prev
            prev = current
        slow = prev
        
        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True