class Solution:
    def superPow(self, a, b):
        MOD = 1337
        
        def mod_pow(x, n):
            res = 1
            x %= MOD
            while n:
                if n % 2:
                    res = (res * x) % MOD
                x = (x * x) % MOD
                n //= 2
            return res
        
        res = 1
        
        for digit in b:
            res = (mod_pow(res, 10) * mod_pow(a, digit)) % MOD
        
        return res