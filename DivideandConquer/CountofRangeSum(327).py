class Solution:
    def countRangeSum(self, nums, lower, upper):
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        def merge_sort(lo, hi):
            if hi - lo <= 1:
                return 0
            
            mid = (lo + hi) // 2
            count = merge_sort(lo, mid) + merge_sort(mid, hi)
            
            j = k = mid
            temp = []
            r = mid
            
            for left in prefix[lo:mid]:
                while k < hi and prefix[k] - left < lower:
                    k += 1
                while j < hi and prefix[j] - left <= upper:
                    j += 1
                count += j - k
            
            # merge step
            l, r = lo, mid
            sorted_temp = []
            while l < mid and r < hi:
                if prefix[l] <= prefix[r]:
                    sorted_temp.append(prefix[l])
                    l += 1
                else:
                    sorted_temp.append(prefix[r])
                    r += 1
            
            sorted_temp.extend(prefix[l:mid])
            sorted_temp.extend(prefix[r:hi])
            
            prefix[lo:hi] = sorted_temp
            return count
        
        return merge_sort(0, len(prefix))