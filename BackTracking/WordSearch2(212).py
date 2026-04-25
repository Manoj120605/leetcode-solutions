class Solution:
    def findWords(self, board, words):
        # Step 1: Build Trie
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node["#"] = word   # end marker
        
        rows, cols = len(board), len(board[0])
        res = []
        
        # Step 2: DFS
        def dfs(r, c, node):
            ch = board[r][c]
            
            if ch not in node:
                return
            
            nxt = node[ch]
            
            # Found a word
            if "#" in nxt:
                res.append(nxt["#"])
                del nxt["#"]   # avoid duplicates
            
            # Mark visited
            board[r][c] = "*"
            
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "*":
                    dfs(nr, nc, nxt)
            
            # Restore
            board[r][c] = ch
            
            
            if not nxt:
                del node[ch]
        
        # Step 3: Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)
        
        return res