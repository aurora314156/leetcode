# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return False
        return self.ValidBST(root, float('-inf'), float('inf'))

    def ValidBST(self, root, Min, Max):
        if not root:
            return True
        if Min >= root.val or root.val >= Max:
            return False
        return self.ValidBST(root.left, Min, root.val) and self.ValidBST(root.right, root.val, Max)