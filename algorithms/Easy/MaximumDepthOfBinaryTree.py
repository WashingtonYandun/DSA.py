# 104. Maximum Depth of Binary Tree
'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # 42ms Beats, 65.63%
    # 17.75MB, beats 85.43%
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [True, 0]
            
            l = dfs(node.left)
            r = dfs(node.right)

            return [ l[0] and r[0] and abs(l[1] - r[1]) < 2 , 1 + max(l[1], r[1])]

        return dfs(root)[1]