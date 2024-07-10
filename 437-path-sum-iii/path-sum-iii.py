# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cnt = 0
        self.check = {}

    def pathSum(self, root: Optional[TreeNode], hh: int) -> int:
        
        def rec(node,start, s):
            if not node:
                return
            s -= node.val
            if s == 0:
                self.cnt += 1
            
            rec(node.left, False, s)
            rec(node.right,False, s)
            if start:
                rec(node.left,True, hh)
                rec(node.right,True, hh)
        rec(root, True, hh)
        return self.cnt
