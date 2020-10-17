# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, ans):
        if root:
            self.inorder(root.left, ans)
            ans.append(root.val)
            self.inorder(root.right, ans)
        return ans
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        return self.inorder(root, ans)