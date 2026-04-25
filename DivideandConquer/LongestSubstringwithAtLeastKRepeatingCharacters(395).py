class Solution:
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0
        
        from collections import Counter
        freq = Counter(s)
        
        for ch in freq:
            if freq[ch] < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(ch))
        
        return len(s)