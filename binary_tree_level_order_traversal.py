# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _levelOrder(self, root, holder, depth):
        if root:
            if len(holder) == depth:
                holder.append([])
            holder[depth].append(root.val)

            self._levelOrder(root.left, holder, depth+1)
            self._levelOrder(root.right, holder, depth+1)
        else:
            return
            
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        holder = []
        depth = 0
        if not root:
            return None
        else:
            self._levelOrder(root, holder, depth)
            return holder
