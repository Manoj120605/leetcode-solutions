class Solution:
    def buildTree(self, inorder, postorder):
        index_map = {val: i for i, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1

        def dfs(left, right):
            if left > right:
                return None

            
            root_val = postorder[self.post_idx]
            self.post_idx -= 1

            root = TreeNode(root_val)

            mid = index_map[root_val]

            
            root.right = dfs(mid + 1, right)
            root.left = dfs(left, mid - 1)

            return root

        return dfs(0, len(inorder) - 1)