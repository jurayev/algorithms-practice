grid = [
    [1,0,0,0,0],
    [0,0,0,1,0],
    [0,0,1,0,0],
    [0,0,0,0,0]
]
rows = 4
columns = 5
def minimumDays(rows, columns, grid):
    new_grid = [[0 for _ in range(columns+2)] for _ in range(rows+2)]
    min_days = 0
    outdated = True
    while outdated:

        active_servers = False
        for row in range(rows):
            if max(grid[row]) == 1:
                active_servers = True
            new_grid[row+1][1:-1] = grid[row]
        if not active_servers:
            return -1

        for r in range(rows):
            if min(grid[r]) == 1:
                outdated = False
                continue
            for c in range(columns):
                if new_grid[r+1][c+1] == 0:
                    outdated = True
                    if new_grid[r+1][c+2] == 1:
                        grid[r][c] = 1
                    elif new_grid[r+1][c] == 1:
                        grid[r][c] = 1
                    elif new_grid[r+2][c+1] == 1:
                        grid[r][c] = 1
                    elif new_grid[r][c+1] == 1:
                        grid[r][c] = 1
        min_days += 1
    return min_days

print(minimumDays(rows, columns, grid))