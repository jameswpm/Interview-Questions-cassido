"""
Given a 2D grid of integers, find the largest sum of any connected path of cells. 
A path consists of horizontally or vertically adjacent cells (no diagonals) and cannot 
reuse cells. Return the largest sum.

Example:

const grid1 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

const grid2 = [
  [5, 3],
  [2, 8]
];

largestPathSum(grid1)
> 45 // (1 → 2 → 3 → 6 → 9 → 8 → 7 → 4 → 5)

largestPathSum(grid2)
> 18 // (5 → 3 → 8 → 2)
"""

def largestPathSum(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    max_sum = [float('-inf')]

    def dfs(r, c, visited, current_sum):
        max_sum[0] = max(max_sum[0], current_sum)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited):
                visited.add((nr, nc))
                dfs(nr, nc, visited, current_sum + grid[nr][nc])
                visited.remove((nr, nc))

    for i in range(rows):
        for j in range(cols):
            visited = set()
            visited.add((i, j))
            dfs(i, j, visited, grid[i][j])

    return max_sum[0]

grid1 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
grid2 = [
  [5, 3],
  [2, 8]
]

print(largestPathSum(grid1))  
print(largestPathSum(grid2))  
        
