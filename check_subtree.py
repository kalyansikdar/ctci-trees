# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Algorithm: 
#   1. If the structure matches with the root, return true.
#   2. Else check if it's a subtree of left subtree or right
#   Note: While checking structure the subtrees of two inputs should match exactly.

class Solution(object):
    def checkStructure(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val == root2.val:    # so that the trees match exactly, even the childrens should be exactly same.
            return self.checkStructure(root1.left, root2.left) and self.checkStructure(root1.right, root2.right)
        else:
            return False

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s:
            if self.checkStructure(s, t):
                return True
            else:
                return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        else:
            return False
