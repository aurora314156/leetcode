# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        slow = fast = head        
        while fast and fast.next:
            cut = slow
            slow = slow.next
            fast = fast.next.next
        cut.next = None
        return self.mergeLinkedList(self.sortList(head), self.sortList(slow))
        
    def mergeLinkedList(self, left, right):
        head = ans = ListNode(0)
        while left and right:
            if left.val < right.val:
                ans.next = left
                left = left.next
            else:
                ans.next = right
                right = right.next
            ans = ans.next
        ans.next = left or right
        return head.next