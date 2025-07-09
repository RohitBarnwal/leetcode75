# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/?envType=study-plan-v2&envId=leetcode-75
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Brute force: make a list with nodes to reach p and q and compare both list. Return last common occurance
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def lcaTraversal(root, p, q):
            if not root or p==root or q==root:
                return root
            left_lca= lcaTraversal(root.left, p, q)
            right_lca= lcaTraversal(root.right, p, q)
            if left_lca and right_lca:
                return root
            return left_lca or right_lca  
            # p and q will exist in the tree. No need to check if only one is there
            # not neccessary to pass p and q- available to small namespace
        # return lcaTraversal(root) # will work too   
        return lcaTraversal(root, p, q)   

# if BST not just any general tree, iterative solution will also work 
#         while root:
#             if p.val>=root.val and q.val>=root.val:
#                 root = root.right
#             elif p.val <= root.val and q.val <= root.val:
#                 root = root.left
#             else:
#                 return root