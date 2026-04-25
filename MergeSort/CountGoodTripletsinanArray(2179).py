class Solution:
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)
        pos = [0] * n
        for i, v in enumerate(nums2):
            pos[v] = i

        arr = [pos[v] for v in nums1]

        bit = [0] * (n + 1)

        def update(i):
            i += 1
            while i <= n:
                bit[i] += 1
                i += i & -i

        def query(i):
            s = 0
            i += 1
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        left = [0] * n
        for i in range(n):
            left[i] = query(arr[i] - 1)
            update(arr[i])

        bit = [0] * (n + 1)

        right = [0] * n
        for i in range(n - 1, -1, -1):
            right[i] = query(n - 1) - query(arr[i])
            update(arr[i])

        res = 0
        for i in range(n):
            res += left[i] * right[i]

        return res