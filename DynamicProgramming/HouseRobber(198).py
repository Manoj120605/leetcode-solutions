class Solution:
    def rob(self, nums):
        prev = 0   
        curr = 0   
        
        for num in nums:
            prev, curr = curr, max(curr, prev + num)
        
        return curr