# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _buildTree(self, start_pre, start_in, end_in, preorder, inorder, inorderIndex):
        
        if start_pre > (len(preorder)-1) or start_in > end_in:
            return
        
        root = TreeNode(preorder[start_pre])
        
        idx = inorderIndex[preorder[start_pre]]
        
        root.left = self._buildTree(start_pre + 1, start_in, idx - 1, preorder, inorder, inorderIndex)
        root.right = self._buildTree(start_pre + (idx - start_in) + 1, idx + 1, end_in, preorder, inorder, inorderIndex)      # Need to find where the right tree should start
        
        return root
    
    
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        start_pre = 0
        start_in = 0
        end_in = len(inorder)-1
        inorderIndex = {}
        
        for idx, i in enumerate(inorder):   # Using dict we can retrieve the index in constant time - O(1)
            inorderIndex[i] = idx
        
        result = self._buildTree(start_pre, start_in, end_in, preorder, inorder, inorderIndex)
        
        return result
