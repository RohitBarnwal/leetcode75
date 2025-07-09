# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/?envType=study-plan-v2&envId=leetcode-75
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def dfs(root, left, longest):
            if not root:
                return 0
            if left:
                longest= max(longest, dfs(root.right,False,longest+1), dfs(root.left,True,1))
            if not left:
                longest= max(longest, dfs(root.left,True,longest+1), dfs(root.right,False,1))
            return longest 
        return max(dfs(root.left,True,1),dfs(root.right,False,1))
