# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        mid = (0+len(nums))//2
        
        root = TreeNode(nums[mid])
        
        if len(nums) == 1:
            return root
        
        root.left = self.sortedArrayToBST(nums[:mid])
        
        if len(nums) == 2:
            return root
        
        root.right = self.sortedArrayToBST(nums[(mid+1):])
        
        return root
