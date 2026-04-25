class Solution:
    def countMajoritySubarrays(self, nums, target):
        arr = [1 if x == target else -1 for x in nums]
        pref = [0]
        for x in arr:
            pref.append(pref[-1] + x)

        vals = sorted(set(pref))
        comp = {v:i for i,v in enumerate(vals)}

        bit = [0]*(len(vals)+1)

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
        for x in pref:
            i = comp[x]
            res += query(i-1)
            update(i)
        return res