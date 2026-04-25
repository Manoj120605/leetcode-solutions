class Solution:
    def isAdditiveNumber(self, num):
        n = len(num)

        for i in range(1, n):
            for j in range(i+1, n):
                if num[0] == '0' and i > 1:
                    break
                if num[i] == '0' and j - i > 1:
                    continue

                a = int(num[:i])
                b = int(num[i:j])
                k = j

                while k < n:
                    c = a + b
                    c_str = str(c)
                    if not num.startswith(c_str, k):
                        break
                    k += len(c_str)
                    a, b = b, c

                if k == n:
                    return True

        return False