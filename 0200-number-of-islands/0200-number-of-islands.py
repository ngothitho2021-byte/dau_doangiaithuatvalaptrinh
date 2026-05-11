class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            # Nếu ra ngoài biên hoặc gặp nước thì dừng
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                return
            grid[i][j] = "0"  # nhấn chìm đất thành nước
            # duyệt 4 hướng
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count
        