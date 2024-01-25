# 100. Same Tree
'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 29ms Beats, 94.43%
    # 16.46MB, beats 67.30%
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inorder(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            if root1.val != root2.val:
                return False
            
            return inorder(root1.left, root2.left) and inorder(root1.right, root2.right)
        
        return inorder(p, q)