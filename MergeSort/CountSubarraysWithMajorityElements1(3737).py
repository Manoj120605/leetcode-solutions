class Solution:
    def countMajoritySubarrays(self, nums, target):
        # Map elements: 1 if it is the target, -1 otherwise.
        # A subarray has target as majority if its sum > 0.
        mapped = [1 if x == target else -1 for x in nums]
        
        # Compute prefix sums
        prefix = [0]
        for val in mapped:
            prefix.append(prefix[-1] + val)
            
        # Use merge sort to count pairs (i, j) with i < j and prefix[i] < prefix[j]
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0
                
            mid = len(arr) // 2
            left, count_left = merge_sort(arr[:mid])
            right, count_right = merge_sort(arr[mid:])
            
            count = count_left + count_right
            
            # Count valid pairs across the split
            j = 0
            for i in range(len(left)):
                while j < len(right) and right[j] <= left[i]:
                    j += 1
                count += len(right) - j
                
            # Merge the two sorted halves
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
                    
            merged.extend(left[i:])
            merged.extend(right[j:])
            
            return merged, count
            
        _, total_valid_subarrays = merge_sort(prefix)
        return total_valid_subarrays