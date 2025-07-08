# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def dfs(root, currentSum, path):
            if not root:
                return False
            currentSum+=root.val
            path.append(root.val)
            if not root.left and not root.right:
                if currentSum==targetSum:
                    ans.append(path.copy())
            dfs(root.left, currentSum, path) 
            dfs(root.right, currentSum, path)
            path.pop()
            
        ans = []
        dfs(root,0,[])
        return ans