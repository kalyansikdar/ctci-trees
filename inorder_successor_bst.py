"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        if not root:
            return None
        
        predecessor = None
        
        while root and root.val != p.val:
            
            if p.val < root.val:
                predecessor = root
                root = root.left
            else:
                root = root.right
                
        # print (predecessor.val, root.val)
        
        if not root:
            return None
        
        if not root.right:
            return predecessor
        else:
            root = root.right
            
            while root.left:
                root = root.left
            return root
            
        
        
