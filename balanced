# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [0, True]
            
            l, r = dfs(node.left), dfs(node.right)
            if abs(l[0] - r[0]) > 1 or not l[1] or not r[1]:
                return [0, False]
            
            return [max(l[0], r[0]) + 1, True]
        
        return dfs(root)[1]
            

        



