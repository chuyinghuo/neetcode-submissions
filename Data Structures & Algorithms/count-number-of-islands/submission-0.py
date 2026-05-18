class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(i, j):
            # Base case: check if out of bounds or at water
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            # Mark the current land as visited
            grid[i][j] = '0'
            # Explore all four directions
            dfs(i + 1, j)  # Down
            dfs(i - 1, j)  # Up
            dfs(i, j + 1)  # Right
            dfs(i, j - 1)  # Left

        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':  # Found an unvisited land
                    dfs(i, j)  # Mark all connected land as visited
                    island_count += 1  # Increment island count

        return island_count

            