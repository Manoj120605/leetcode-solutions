class Solution:
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        max_len = max(map(len, wordDict)) if wordDict else 0
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]

            res = []
            for end in range(start + 1, min(len(s), start + max_len) + 1):
                word = s[start:end]
                if word in word_set:
                    for sub in dfs(end):
                        res.append(word + (" " + sub if sub else ""))
            
            memo[start] = res
            return res

        return dfs(0)