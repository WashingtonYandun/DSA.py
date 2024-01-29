# 101. Symmetric Tree
'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 37ms Beats, 72.31%
    # 16.51MB, beats 62.50%
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            
            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
        
        return dfs(root.left, root.right)