"""
Algorithm:
  1. If root is there, go push nodes into stack, root = root.left
  2. If root is null, pop from stack and store in result
  3. make root = root.right
  4. Repeat 1,2,3
"""
def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        
        stack = []
        result = []
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right
            
        return result
