# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.s = 0
        def rec(node):
            if node:
                rec(node.right)
                self.s += node.val
                node.val = self.s
                rec(node.left)
        rec(root)
        return root