# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def rec(node):
            leaves = []
            if not node.left and not node.right:
                return [node.val]
            
            if node.left:
                leaves = leaves + rec(node.left)
            
            if node.right:
                leaves = leaves + rec(node.right)
            return leaves
        return rec(root1) == rec(root2)

