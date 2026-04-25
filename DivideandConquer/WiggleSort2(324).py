class Solution:
    def wiggleSort(self, nums):
        n = len(nums)
        sorted_nums = sorted(nums)
        
        mid = (n + 1) // 2
        
        small = sorted_nums[:mid][::-1]
        large = sorted_nums[mid:][::-1]
        
        i = j = 0
        
        for k in range(n):
            if k % 2 == 0:
                nums[k] = small[i]
                i += 1
            else:
                nums[k] = large[j]
                j += 1