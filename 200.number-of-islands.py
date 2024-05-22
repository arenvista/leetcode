# @leet start
class Solution:
    def BFS(self, grid: List[List[str]], i: int, j: int):
        # if i or j are beyond the scope just return
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == "0":
            return
        
        #try and search up and down, the func will just return when we hit off grid
        grid[i][j] = "0"
        self.BFS(grid, i+1, j) # up
        self.BFS(grid, i-1, j) # down
        self.BFS(grid, i, j+1) # right
        self.BFS(grid, i, j-1) # left
        



    def numIslands(self, grid: List[List[str]]) -> int:
        count: int = 0
        N_i = len(grid)
        N_j = len(grid[0])
        N = len(grid)

        for i in range(N_i):
            for j in range(N_j):
                if grid[i][j] == "1":
                    count += 1
                    self.BFS(grid, i, j)
        return count

                    



# @leet end
