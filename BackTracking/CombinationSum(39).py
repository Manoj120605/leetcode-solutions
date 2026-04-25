class Solution:
    def combinationSum(self, candidates, target):
        res = []
        
        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                # choose
                path.append(candidates[i])
                
                # stay at i (reuse allowed)
                backtrack(i, path, remaining - candidates[i])
                
                # undo
                path.pop()
        
        backtrack(0, [], target)
        return res