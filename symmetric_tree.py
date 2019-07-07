# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkSymmetry(self, root1, root2):
        # print (root1.val, root2.val)
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val == root2.val:
            return self.checkSymmetry(root1.left, root2.right) and self.checkSymmetry(root2.left, root1.right)
        else:
            return False
        
    def isSymmetric(self, root):
        """ 
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.checkSymmetry(root.left, root.right)
