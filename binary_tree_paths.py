# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _binaryTreePaths(self, root, holder, temp):
        if root:
            temp += str(root.val)
            if not root.left and not root.right:
                # when both children are null, then only add the path to the result
                holder.append(temp)
                temp = ""
                return
            if root.left:
                self._binaryTreePaths(root.left, holder, temp + "->")
            if root.right:
                self._binaryTreePaths(root.right, holder, temp + "->")
            
                
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        temp = ""
        if not root:
            return None
        else:
            self._binaryTreePaths(root, result, temp)
            return result
