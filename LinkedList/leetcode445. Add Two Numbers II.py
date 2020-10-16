# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def getNum(node):
            l = []
            while node:
                l.append(str(node.val))
                node = node.next
            return int(''.join(l))
        res = getNum(l1) + getNum(l2)
        ans = [int(num) for num in str(res)]
        head = dummy = ListNode(0)
        while ans:
            dummy.next = ListNode(ans.pop(0))
            dummy = dummy.next
        return head.next