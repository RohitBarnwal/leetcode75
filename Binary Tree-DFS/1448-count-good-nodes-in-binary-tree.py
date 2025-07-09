# https://leetcode.com/problems/count-good-nodes-in-binary-tree/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def update_with_highest_value(root, maxi):
            if not root:
                return 0
            good =0
            if root.val>=maxi:
                good =1 
            maxi = max(root.val, maxi)
            return good+update_with_highest_value(root.left, maxi)+update_with_highest_value(root.right, maxi)
        return update_with_highest_value(root, root.val)
