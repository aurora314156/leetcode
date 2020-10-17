# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n: return head
        dummyNode = current = ListNode(0)
        dummyNode.next = head
        for _ in range(m-1):
            current = current.next
        
        rev_prev = None
        cur = current.next
        for _ in range(n-m+1):
            rev_head = cur.next
            cur.next = rev_prev
            rev_prev = cur
            cur = rev_head
        current.next.next = cur
        current.next = rev_prev 
        
        return dummyNode.next