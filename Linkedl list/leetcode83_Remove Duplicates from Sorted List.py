# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        list_head = ListNode(0)
        list_head.next = head
        pre_p = head
        while pre_p:
            cur_p = pre_p.next
            while cur_p and pre_p.val == cur_p.val:
                cur_p = cur_p.next
            pre_p.next = cur_p
            pre_p = cur_p
            
        return list_head.next
            