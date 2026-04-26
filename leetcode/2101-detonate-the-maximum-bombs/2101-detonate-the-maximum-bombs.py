class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in range(n)]
        
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                
                if (x1 - x2)**2 + (y1 - y2)**2 <= r1**2:
                    graph[i].append(j)
        
        def dfs(node, visited):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei, visited)
        
        res = 0
        
        for i in range(n):
            visited = set()
            dfs(i, visited)
            res = max(res, len(visited))
        
        return res
