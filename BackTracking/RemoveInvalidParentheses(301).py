class Solution:
    def removeInvalidParentheses(self, s):
        from collections import deque

        def is_valid(st):
            bal = 0
            for ch in st:
                if ch == '(':
                    bal += 1
                elif ch == ')':
                    bal -= 1
                    if bal < 0:
                        return False
            return bal == 0

        res = []
        visited = set([s])
        q = deque([s])
        found = False

        while q:
            cur = q.popleft()

            if is_valid(cur):
                res.append(cur)
                found = True

            if found:
                continue

            for i in range(len(cur)):
                if cur[i] not in '()':
                    continue
                nxt = cur[:i] + cur[i+1:]
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

        return res