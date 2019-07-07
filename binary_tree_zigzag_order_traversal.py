# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _zigzagLevelOrder(self, root, result, depth):
        if root:
            if len(result) == depth:
                result.append([])
            if depth%2 == 0:
                result[depth].append(root.val)
            else:
                result[depth].insert(0, root.val)
            self._zigzagLevelOrder(root.left, result, depth+1)
            self._zigzagLevelOrder(root.right, result, depth+1)
        else:
            return
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        depth = 0
        if not root:
            return None
        else:
            self._zigzagLevelOrder(root, result, depth)
            return result
