# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, currentSum):
            if not root:
                return False
            currentSum+=root.val
            if not root.left and not root.right:
                if currentSum==targetSum:
                    return True
            return dfs(root.left, currentSum) or dfs(root.right, currentSum)
        return dfs(root,0)