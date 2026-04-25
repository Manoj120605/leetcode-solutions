class Solution:
    def countSmaller(self, nums):
        # Coordinate compression
        ranks = {v: i+1 for i, v in enumerate(sorted(set(nums)))}
        
        size = len(ranks)
        bit = [0] * (size + 1)
        
        def update(i):
            while i <= size:
                bit[i] += 1
                i += i & -i
        
        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s
        
        res = []
        
        # traverse from right
        for num in reversed(nums):
            idx = ranks[num]
            res.append(query(idx - 1)) 
            update(idx)
        
        return res[::-1]