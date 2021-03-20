# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = parent =  ListNode(0)
        dummy.next = head
        while parent.next:
            cur = parent.next
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if parent.next != cur:
                parent.next = cur.next
            else:
                parent = parent.next
        return dummy.next