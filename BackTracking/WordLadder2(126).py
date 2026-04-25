from collections import defaultdict

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        # Track parents for each word to easily build paths backwards
        parents = defaultdict(set)
        
        layer = {beginWord}
        wordSet.discard(beginWord)
        
        found = False
        while layer and not found:
            next_layer = set()
            
            for word in layer:
                word_chars = list(word)
                for i in range(len(word_chars)):
                    orig_char = word_chars[i]
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        if char == orig_char:
                            continue
                        
                        word_chars[i] = char
                        next_word = "".join(word_chars)
                        
                        if next_word in wordSet:
                            next_layer.add(next_word)
                            parents[next_word].add(word)
                            
                            if next_word == endWord:
                                found = True
                    
                    word_chars[i] = orig_char  # backtrack character
            
            # Remove all words visited in this layer to prevent longer paths
            wordSet -= next_layer
            layer = next_layer
        
        res = []
        if not found:
            return res
            
        # DFS backward to avoid dead ends
        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            
            for p in parents[word]:
                dfs(p, path + [p])
                
        dfs(endWord, [endWord])
        return res