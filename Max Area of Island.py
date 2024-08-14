class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        max_area = 0

        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or (r, c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r, c))
            
            area = 1
            
            area += dfs(r, c + 1)
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c - 1)
            
            return area

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == 1:
                    cur_area = dfs(r, c)
                    max_area = max(max_area, cur_area)
        
        return max_area
