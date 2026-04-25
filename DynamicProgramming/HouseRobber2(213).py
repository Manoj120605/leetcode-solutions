class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        def rob_line(arr):
            prev = 0
            curr = 0
            for num in arr:
                prev, curr = curr, max(curr, prev + num)
            return curr
        
        return max(rob_line(nums[:-1]), rob_line(nums[1:]))