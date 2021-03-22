class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        col_len, row_len = len(grid), len(grid[0])
        islands = 0
        for i in range(col_len):
            for j in range(row_len):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j, col_len, row_len)
                    islands += 1
        return islands
    
    def dfs(self, grid, x, y, col_limit, row_limit):
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        grid[x][y] = '0'
        for i, j in directions:
            next_x = x + i
            next_y = y + j
            if -1 < next_x and -1 < next_y and next_x < col_limit and next_y < row_limit:
                if grid[next_x][next_y] == '1':
                    self.dfs(grid, next_x, next_y, col_limit, row_limit)
        