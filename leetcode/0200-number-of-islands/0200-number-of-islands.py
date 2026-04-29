class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direct = [(0, 1), (0, -1) , (1, 0) , (-1, 0)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        count = [0]
        
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        def dfs(grid, visited, row, col):
            visited[row][col] = True

            for x, y in direct:
                nr = x + row
                nc = y + col
            
                if inbound(nr, nc) and grid[nr][nc] == '1' and not visited[nr][nc]:
                    dfs(grid, visited, nr, nc)
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == '1':
                    count[0] += 1
                    dfs(grid, visited, i, j)
        return count[0]