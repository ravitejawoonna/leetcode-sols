# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
        
        def rec(node):
            if not node:
                return False
    
            if node.val == sub.val:
                if self.areSame(sub, node): return True
            
            return rec(node.left) or rec(node.right)
        
        return rec(root)
    
    def areSame(self, p, q):

        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.areSame(p.left, q.left) and self.areSame(p.right, q.right)