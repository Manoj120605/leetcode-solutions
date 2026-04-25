class Solution:
    def restoreIpAddresses(self, s):
        res = []
        
        def backtrack(start, path):
            # If we got 4 parts
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return
            
            # Try lengths 1 to 3
            for l in range(1, 4):
                if start + l > len(s):
                    break
                
                part = s[start:start + l]
                
                
                if part[0] == '0' and len(part) > 1:
                    continue
                
                
                if int(part) > 255:
                    continue
                
                backtrack(start + l, path + [part])
        
        backtrack(0, [])
        return res