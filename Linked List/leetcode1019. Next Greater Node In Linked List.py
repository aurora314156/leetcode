# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        s = []
        res = [0] * len(l)
        for ind, val in enumerate(l):
            while s and l[s[-1]] < val:
                res[s.pop()] = val
            s.append(ind)
        return res