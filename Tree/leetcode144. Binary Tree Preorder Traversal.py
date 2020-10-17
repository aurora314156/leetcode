# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root, ans):
            if root:
                ans.append(root.val)
                preorder(root.left, ans)
                preorder(root.right, ans)
            return ans
        ans = []
        return preorder(root, ans)