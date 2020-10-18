# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        Alen, Blen = self.getLen(headA), self.getLen(headB)
        if Alen < Blen:
            for _ in range(Blen-Alen):
                headB = headB.next
        else:
            for _ in range(Alen-Blen):
                headA = headA.next
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
    
    def getLen(self, node):
        l = 0
        while node:
            l+=1
            node = node.next
        return l