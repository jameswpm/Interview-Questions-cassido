"""
You're given a 2D grid representing a city where each cell is either empty (0), a fire station (1), or a building (2). 
Fire stations can serve buildings based on horizontal + vertical moves only. 
Return a 2D grid where each cell shows the minimum distance to the nearest fire station.

Examples:

> fireStationCoverage([
  [2, 0, 1],
  [0, 2, 0],
  [1, 0, 2]
])
> [[2, 1, 0],  
   [1, 2, 1],
   [0, 1, 2]]

> fireStationCoverage([
  [1, 0, 0, 1],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [1, 0, 0, 1]
])
> [[0, 1, 2, 0],
   [1, 2, 2, 1],
   [1, 2, 2, 1],
   [0, 1, 2, 0]]
"""

from collections import deque

def fire_station_coverage(grid: list) -> list:
    rows, cols = len(grid), len(grid[0])
    
    dist = [[-1] * cols for _ in range(rows)] # the result grid started with -1 for all cells
    queue = deque()

    # mark all fire stations with distance 0 and add them to the queue
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                dist[r][c] = 0
                queue.append((r, c))
    
    # directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        current_row, current_col = queue.popleft()
        current_dist = dist[current_row][current_col]

        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and dist[new_row][new_col] == -1:
                dist[new_row][new_col] = current_dist + 1
                queue.append((new_row, new_col))

    return dist

if __name__ == "__main__":
    assert fire_station_coverage([
        [2, 0, 1],
        [0, 2, 0],
        [1, 0, 2]
    ]) == [[2, 1, 0],  
          [1, 2, 1],
          [0, 1, 2]]


    print(fire_station_coverage([
        [1, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 1]
    ]))
    assert fire_station_coverage([
        [1, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 1]
    ]) == [[0, 1, 2, 0],
          [1, 2, 2, 1],
          [1, 2, 2, 1],
          [0, 1, 2, 0]]
    
    # Additional test cases
    assert fire_station_coverage([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]) == [[2, 1, 2],
          [1, 0, 1],
          [2, 1, 2]]
    
    assert fire_station_coverage([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]) == [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
    
    assert fire_station_coverage([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]) == [[-1, -1, -1],
          [-1, -1, -1],
          [-1, -1, -1]]
    print("All tests passed")