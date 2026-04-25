import random

class Solution:
    def findKthLargest(self, nums, k):
        k = len(nums) - k
        
        def quickselect(l, r):
            pivot = nums[random.randint(l, r)]
            
            
            i, lt, gt = l, l, r
            
            while i <= gt:
                if nums[i] < pivot:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    i += 1
                    lt += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1
            
            
            
            if k < lt:
                return quickselect(l, lt - 1)
            elif k > gt:
                return quickselect(gt + 1, r)
            else:
                return nums[k]
        
        return quickselect(0, len(nums) - 1)