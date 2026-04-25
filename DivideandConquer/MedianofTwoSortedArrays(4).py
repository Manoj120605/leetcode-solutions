class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left = (m + n + 1) // 2
        
        lo, hi = 0, m
        
        while lo <= hi:
            i = (lo + hi) // 2
            j = left - i
            
            Aleft = nums1[i-1] if i > 0 else float('-inf')
            Aright = nums1[i] if i < m else float('inf')
            Bleft = nums2[j-1] if j > 0 else float('-inf')
            Bright = nums2[j] if j < n else float('inf')
            
            if Aleft <= Bright and Bleft <= Aright:
                if (m + n) % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
                else:
                    return float(max(Aleft, Bleft))
            
            elif Aleft > Bright:
                hi = i - 1
            else:
                lo = i + 1