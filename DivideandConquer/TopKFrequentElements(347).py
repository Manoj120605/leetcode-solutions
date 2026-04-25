class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter
        
        freq = Counter(nums)
        
        # bucket: index = frequency
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for num, f in freq.items():
            bucket[f].append(num)
        
        res = []
        
        # traverse from high freq
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res