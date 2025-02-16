# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            return max(height(node.left), height(node.right)) + 1
        if not root:
            return True
        
        l, r = height(root.left), height(root.right)
        if abs(l-r) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        



