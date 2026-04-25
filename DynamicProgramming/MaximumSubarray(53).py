class Solution:
    def maxSubArray(self, nums):
        cur = nums[0]
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            cur = max(nums[i], cur + nums[i])
            max_sum = max(max_sum, cur)
        
        return max_sum