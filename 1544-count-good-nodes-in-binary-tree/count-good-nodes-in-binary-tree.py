# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def rec(node, maxVal):
            count = 0
            if not node:
                return 0

            if node.val >= maxVal:
                count += 1
            maxVal = max(maxVal, node.val)

            count += rec(node.left, maxVal)
            count += rec(node.right, maxVal)
            return count
        
        return rec(root, root.val)