# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        Len = 0
        tmp = root
        while tmp:
            Len+=1
            tmp = tmp.next
        part_len = Len // k
        remain = Len % k
        
        res = []
        for _ in range(k):
            head = ListNode(0)
            each = head
            for _ in range(part_len):
                node = ListNode(root.val)
                each.next = node
                each = each.next
                root = root.next
            if remain and root:
                remain_node = ListNode(root.val)
                each.next = remain_node
                if root:
                    root = root.next
                remain -= 1
            res.append(head.next)
        return res