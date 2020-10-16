# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://skyyen999.gitbooks.io/-leetcode-with-javascript/content/questions/24md.html
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev_p = dummy
        cur_p = head
        while cur_p and cur_p.next:
            keep_p = cur_p.next.next # keep 3 -> 4
            cur_p.next.next = cur_p # let 1 -> 2 -> 3... become ->1 -> 2 -> 1
            # nil -> 1 -> 2 become head -> 2 -> 1 -> 2
            prev_p.next = cur_p.next
            # head -> 2 -> 1 -> 3 -> 4
            cur_p.next = keep_p
            prev_p = cur_p
            cur_p = cur_p.next
        return dummy.next
            
            
            
            
            