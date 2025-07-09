# https://leetcode.com/problems/leaf-similar-trees/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaf(root, leaf_nodes):

            if not root:
                return 
            if not (root.left or root.right):
                leaf_nodes.append(root.val)
                return
            getLeaf(root.left, leaf_nodes)
            getLeaf(root.right, leaf_nodes)

        leaf_nodes1 = []
        getLeaf(root1, leaf_nodes1)

        leaf_nodes2 = []
        getLeaf(root2, leaf_nodes2)

        if leaf_nodes1==leaf_nodes2:
            return True
        return False