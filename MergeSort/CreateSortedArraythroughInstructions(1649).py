class Solution:
    def createSortedArray(self, instructions):
        max_val = max(instructions)
        size = max_val + 1
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

        res = 0
        mod = 10**9 + 7

        for x in instructions:
            left = query(x - 1)
            right = query(size) - query(x)
            res = (res + min(left, right)) % mod
            update(x)

        return res