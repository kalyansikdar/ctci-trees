# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _hasPathSum(self, root, holder, value):
        if root:
            value += root.val
            if not root.left and not root.right:
                holder.append(value)
            
            self._hasPathSum(root.left, holder, value)
            self._hasPathSum(root.right, holder, value)
        else:
            return
        
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        holder = []
        value = 0
        if not root:
            return False
        else:
            self._hasPathSum(root, holder, value)
            if sum in holder:
                return True
            else:
                return False
