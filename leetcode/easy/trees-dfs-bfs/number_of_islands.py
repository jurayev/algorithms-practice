from collections import deque

def num_of_islands(grid):
    if not grid or not grid[0]:
        return 0

    r = len(grid)
    c = len(grid[0])

    islands = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == "1":
                islands += 1
                #bfs(grid, i, j, r, c)
                dfs(grid, i, j, r, c)
    print_map(grid)
    return islands

#Time O(n^2) Space O(n)
def bfs(grid, i, j, r, c):
    q = deque([(i, j)])
    while q:
        adj = q.popleft()
        new_i, new_j = adj[0], adj[1]
        if grid[new_i][new_j] == "1":
            grid[new_i][new_j] = "2"
            append_if(grid, q, new_i, new_j + 1, r, c)
            append_if(grid, q, new_i, new_j - 1, r, c)
            append_if(grid, q, new_i + 1, new_j, r, c)
            append_if(grid, q, new_i - 1, new_j, r, c)

def append_if(grid, q, i, j, r, c):
    if 0 <= i < r and 0 <= j < c and grid[i][j] == "1":
        q.append([i, j])

def print_map(grid):
    for row in grid:
        print(row)

#Time O(n^2) Space O(1)
def dfs(grid, i, j, rows, columns):
    if 0 <= i < rows and 0 <= j < columns and grid[i][j] == "1":
        grid[i][j] = "2"
        dfs(grid, i, j + 1, rows, columns)
        dfs(grid, i, j - 1, rows, columns)
        dfs(grid, i + 1, j, rows, columns)
        dfs(grid, i - 1, j, rows, columns)


test_grid = [["1","1","1","1","0"],
             ["1","1","0","1","0"],
             ["1","1","0","0","1"],
             ["0","0","0","0","1"]]

test_grid_2 = [["1","1","1","1","1","1","1"],
                ["0","0","0","0","0","0","1"],
                ["1","1","1","1","1","0","1"],
                ["1","0","0","0","1","0","1"],
                ["1","0","1","0","1","0","1"],
                ["1","0","1","1","1","0","1"],
                ["1","1","1","1","1","1","1"]]
print(num_of_islands(test_grid_2))
