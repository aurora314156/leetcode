# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def tmpCount(sumN, l):
            digit, i = 0, 0
            while l:
                v = l.val
                l = l.next
                sumN += v * pow(10, i)
                i+=1
            return sumN
    
        sumN = 0
        sumN = tmpCount(sumN, l1) + tmpCount(sumN, l2)
        
        head = node = ListNode(0)
        while sumN:
            tmpN = sumN % 10
            node.next = ListNode(tmpN)
            node = node.next
            sumN//= 10
        # if sum has more than one digit
        if head.next is not None:
            return head.next
        else:
            return head