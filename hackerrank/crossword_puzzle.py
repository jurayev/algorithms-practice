grid = [
    ['-', '-', '-', '-', '+'],
    ['+', '-', '+', '+', '+'],
    ['+', '-', '+', '+', '+'],
    ['+', '-', '-', '-', '-'],
    ['+', '-', '+', '+', '+']
]
words = [
    'movie',
    'aman',
    'imma'
]


def print_board(grid):
    for row in grid:
        print(''.join(row))

def find_coordinates(grid, word):
    possible_cells = []
    word_length = len(word)
    grid_length = len(grid)
    # horizontal match
    for i in range(grid_length):
        for j in range(grid_length - word_length + 1):
            proper_cell = True
            for k in range(word_length):
                if grid[i][j + k] not in ['-', word[k]]:
                    proper_cell = False
                    break
            if proper_cell:
                possible_cells.append([i, j, 0])
                break

    # vertical match
    for i in range(grid_length - word_length + 1):
        for j in range(grid_length):
            proper_cell = True
            for k in range(word_length):
                if grid[i + k][j] not in ['-', word[k]]:
                    proper_cell = False
                    break
            if proper_cell:
                possible_cells.append([i, j, 1])
                break
    return possible_cells

def fill_board(grid, word, possible_cell):
    i, j, axis = possible_cell
    word_length = len(word)
    if axis == 0:
        for k in range(word_length):
            grid[i][j + k] = word[k]
    else:
        for k in range(word_length):
            grid[i + k][j] = word[k]

def rollback(grid, word, rollback_cell):
    i, j, axis = rollback_cell
    word_length = len(word)
    if axis == 0:
        for k in range(word_length):
            grid[i][j + k] = '-'
    else:
        for k in range(word_length):
            grid[i + k][j] = '-'

def solve_crossword(grid, words):
    global is_solved
    if len(words) == 0:
        if not is_solved:
            print_board(grid)
        is_solved = True
        return

    word = words.pop()

    coordinates = find_coordinates(grid, word)
    for coordinate in coordinates:
        fill_board(grid, word, coordinate)
        solve_crossword(grid, words)
        rollback(grid, word, coordinate)

    words.append(word)

is_solved = False
solve_crossword(grid, words)

# '+a+',
# '+ba',
# '+a+',


# +L++++++++
# +O++++++++
# +N++++++++
# +DELHI++++
# +O+++C++++
# +N+++E++++
# +++++L++++
# ++ANKARA++
# +++++N++++
# +++++D++++
