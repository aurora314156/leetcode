# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head and head.next:
            # get middle head of listnode
            fast = slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            new_head = slow.next
            slow.next = None

            # reverse half of listnode
            prev = None
            while new_head:
                current = new_head
                new_head = new_head.next
                current.next = prev
                prev = current
            new_head = prev

            # merge two listnode
            p1 = head
            p2 = new_head
            while p2:
                tmp_p1 = p1.next
                tmp_p2 = p2.next
                p1.next = p2
                p2.next = tmp_p1
                p1 = tmp_p1
                p2 = tmp_p2