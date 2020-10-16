# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.binarySearchTree(nums)
        
    def binarySearchTree(self, nums):
        if not nums: return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.binarySearchTree(nums[:mid])
        node.right = self.binarySearchTree(nums[mid+1:])
        return node
    