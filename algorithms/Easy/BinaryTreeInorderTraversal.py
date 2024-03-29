# 94. Binary Tree Inorder Traversal
'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 30ms Beats, 94.19%
    # 16.45MB, beats 35.07%
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(root):
            if root is None:
                return None
            
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        
        inorder(root)
        
        return res
            