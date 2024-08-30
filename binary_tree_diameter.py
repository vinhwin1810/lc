# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(root):
            nonlocal res

            if not root:
                return 0
            
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            
            res = max(res, left_height + right_height) 
            
            return max(left_height, right_height) + 1 
            #return depth because each node we want to find diameter, which is depth left + right depth
        
        dfs(root)
        return res
        
        
        

        
