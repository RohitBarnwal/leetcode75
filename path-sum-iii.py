# https://leetcode.com/problems/path-sum-iii/?envType=study-plan-v2&envId=leetcode-75
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(root, currentSum,sum_dict):

            if not root:
                return 0
            currentSum+=root.val
            count = sum_dict.get(currentSum-targetSum,0)
            sum_dict[currentSum] = sum_dict.get(currentSum,0)+1
            left = dfs(root.left, currentSum, sum_dict)
            right = dfs(root.right, currentSum, sum_dict)
            # backtrack last entry in dictionary
            sum_dict[currentSum]-=1
            return left+count+right

        sum_dict={0:1}
        # since dictionary mutable object- okay to pass or not pass. It will be accessible to inner function namespace
        # dfs(root, 0) #will also work 
        return dfs(root,0,sum_dict)