# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_dep = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def rec(node, dep):
            if not node:
                return dep
            return max(
                rec(node.left, dep+1),
                rec(node.right, dep+1)
            )
        return rec(root, 0)