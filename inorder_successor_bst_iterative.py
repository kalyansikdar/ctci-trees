"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
"""
Algorithm:
    1. Find the node
    2. If the node does not have a right child, go up till the value is greater that the node
    3. If the node has a right child, go to the right child. Then return the extreme left child of the right child. 
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
            
        
        
