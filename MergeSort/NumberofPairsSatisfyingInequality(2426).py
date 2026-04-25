class Solution:
    def numberOfPairs(self, nums1, nums2, diff):
        arr = [a - b for a, b in zip(nums1, nums2)]
        vals = sorted(set(arr + [x - diff for x in arr]))
        idx = {v: i for i, v in enumerate(vals)}

        bit = [0] * (len(vals) + 1)

        def update(i):
            i += 1
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def query(i):
            s = 0
            i += 1
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        res = 0
        for x in arr:
            target = x + diff
            import bisect
            j = bisect.bisect_right(vals, target) - 1
            if j >= 0:
                res += query(j)
            update(idx[x])
        return res