class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # giả định có 4 cạnh
                    perimeter += 4
                    # nếu có đất bên trên thì trừ đi 2 cạnh chung
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    # nếu có đất bên trái thì trừ đi 2 cạnh chung
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2

        return perimeter