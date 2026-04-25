class Solution:
    def pathSum(self, root, targetSum):
        res = []
        
        def dfs(node, remaining, path):
            if not node:
                return
            
            # Add current node
            path.append(node.val)
            remaining -= node.val
            
            # Check leaf
            if not node.left and not node.right and remaining == 0:
                res.append(path[:])   # copy
            
            # Traverse
            dfs(node.left, remaining, path)
            dfs(node.right, remaining, path)
            
            # Backtrack
            path.pop()
        
        dfs(root, targetSum, [])
        return res