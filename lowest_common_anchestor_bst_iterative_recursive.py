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
        # This iterative solution is BST specific
        """
        Algorithm:
        # while root:
        # both nodes are smaller than the root, go left
        # both nodes are greater than the root, go right
        # else root is LCA
        """
        while root:
            if root.val > p.val and root.val > q.val:        
                root = root.left
            elif p.val > root.val and q.val > root.val:      
                root = root.right
            else:
                return root
            
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # This recursive solution is BST specific
        """
        Algorithm:
        # both nodes are smaller than the root, go left
        # both nodes are greater than the root, go right
        # else root is LCA
        """
        
        if root.val > p.val and root.val > q.val:        
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:      
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

