class Solution:
    def countDigitOne(self, n):
        count = 0
        d = 1  # digit place
        
        while d <= n:
            high = n // (d * 10)
            cur = (n // d) % 10
            low = n % d
            
            if cur == 0:
                count += high * d
            elif cur == 1:
                count += high * d + low + 1
            else:
                count += (high + 1) * d
            
            d *= 10
        
        return count