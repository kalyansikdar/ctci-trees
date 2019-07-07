# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root, result):
        if root:
            self.inorderTraversal(root.left, result)
            result.append(root.val)
            self.inorderTraversal(root.right, result)
        else:
            return
        
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return None
        else:
            result = []
            self.inorderTraversal(root, result)
            return result[k-1]
