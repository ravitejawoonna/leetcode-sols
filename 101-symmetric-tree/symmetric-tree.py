# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def rec(p,q):
            if not p and not q:
                return True
            
            if not q or not p:
                return False
            
            if q.val != p.val:
                return False
            
            return rec(p.left, q.right) and rec(p.right, q.left)
        return rec(
            root.left, root.right
        )