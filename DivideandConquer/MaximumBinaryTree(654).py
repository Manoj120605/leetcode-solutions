class Solution:
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None
        
        max_val = max(nums)
        idx = nums.index(max_val)
        
        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx+1:])
        
        return root