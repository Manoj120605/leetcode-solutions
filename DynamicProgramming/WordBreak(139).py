class Solution:
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        max_len = max(map(len, wordDict)) if wordDict else 0
        
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for l in range(1, min(i, max_len) + 1):
                if dp[i - l] and s[i - l:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[len(s)]