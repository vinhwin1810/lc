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
                return 0
            l, r = dfs(node.left), dfs(node.right)

            if abs(l-r) > 1 or l == 33 or r == 33:
                return 33
            
            return max(l,r) + 1
        
        return dfs(root) != 33
            
