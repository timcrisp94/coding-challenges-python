# - pseudo -
# def numIslands(grid)
# IF NOT grid return 0
# count = 0
# FOR i in range(len(grid))
#   FOR j in range(len(grid[0]))
#     IF grid[i][j] == '1'
#       self.dfs(grid, i, j)
#       count += 1
# return count
# def dfs(grid, i, j)
# IF i < 0 OR i >= len(grid) OR j >= len(grid[0]) or grid[i][j] != '1' return
# grid[i][j] = '#'
#  self.dfs(grid, i+1, j)
#  self.dfs(grid, i-1, j)
#  self.dfs(grid, i, j+1)
#  self.dfs(grid, i, j-1)  

def numIslands(self, grid):
    if not grid:
        return 0
        
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                self.dfs(grid, i, j)
                count += 1
    return count

def dfs(self, grid, i, j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
        return
    grid[i][j] = '#'
    self.dfs(grid, i+1, j)
    self.dfs(grid, i-1, j)
    self.dfs(grid, i, j+1)
    self.dfs(grid, i, j-1)