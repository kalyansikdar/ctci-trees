"""
Algorithm:
1. If either of the nodes are equal to the root, then root is the LCA
2. Else, check LCA for its left and right children
3. If both left node or right node returns a value, then root is the LCA
4. If only left or right node returns a value, then left or right is LCA respectively
Link: https://www.youtube.com/watch?v=13m9ZCB8gjw
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        if root == p or root == q:      # if either of the roots are equal to root, root is the LCA
            return root
        
        nodeLeft = self.lowestCommonAncestor(root.left, p, q)
        nodeRight = self.lowestCommonAncestor(root.right, p, q)
        
        if nodeLeft and nodeRight:
            return root     # in case returns from both left and right side is not null, then root is the LCA
        if not nodeLeft and not nodeRight:
            return None
        if not nodeLeft:        # if left is not nulll, return left, otherwise return right
            return nodeRight
        else:
            return nodeLeft
