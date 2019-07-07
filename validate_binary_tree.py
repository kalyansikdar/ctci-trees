import sys
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root, leftLimit = (-sys.maxint+1), rightLimit = sys.maxint):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            leftVal = root.left.val if root.left else leftLimit
            rightVal = root.right.val if root.right else rightLimit
            
            if leftVal < root.val < rightVal:       # left node in the sub-trees should be smaller than main root value
                return self.isValidBST(root.left, leftLimit, root.val) and self.isValidBST(root.right, root.val, rightLimit)
            else:
                return False
        else:
            return True
