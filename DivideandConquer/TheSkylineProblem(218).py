import heapq
from collections import Counter

class Solution:
    def getSkyline(self, buildings):
        events = []
        
        for l, r, h in buildings:
            events.append((l, -h))
            events.append((r, h))
        
        events.sort()
        
        res = []
        heap = [0]  
        count = Counter({0:1})
        prev_max = 0
        
        for x, h in events:
            if h < 0:
                heapq.heappush(heap, h)
                count[-h] += 1
            else:
                count[h] -= 1
            
            while heap and count[-heap[0]] == 0:
                heapq.heappop(heap)
            
            curr_max = -heap[0]
            
            if curr_max != prev_max:
                res.append([x, curr_max])
                prev_max = curr_max
        
        return res
