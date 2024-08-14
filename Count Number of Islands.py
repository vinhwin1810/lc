class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        island = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        # dfs on a cell with coordinates (i, j)
        def dfs(i, j):
            # Check if the cell is out of bounds or is water or already visited
            if (i < 0 or i >= rows or j < 0 or j >= cols or
                    grid[i][j] == '0' or (i, j) in visited):
                return
            
            visited.add((i, j))
            
            # Explore all 4 possible directions
            dfs(i, j + 1)  # right
            dfs(i + 1, j)  # down
            dfs(i - 1, j)  # up
            dfs(i, j - 1)  # left

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    island += 1
                    dfs(i, j)
                    
        return island
