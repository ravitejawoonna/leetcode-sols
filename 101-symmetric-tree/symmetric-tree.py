# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        q = [root]

        while q:
            nq = []
            s = []
            for item in q:
                if not item:
                    s = s + ["*"]
                    continue
                s = s + [str(item.val)]
                nq.append(item.left)
                nq.append(item.right)
            if s != s[::-1]:
                return False
            q = nq
        return True