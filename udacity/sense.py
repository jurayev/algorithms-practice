import numpy as np


def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = np.zeros((len(grid), len(grid[0])))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == color:
                new_beliefs[i][j] = beliefs[i][j] * p_hit
            else:
                new_beliefs[i][j] = beliefs[i][j] * p_miss

    total_p = np.sum(new_beliefs)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            new_beliefs[i][j] = new_beliefs[i][j] / total_p

    #print(new_beliefs)
    return new_beliefs

R = 'r'
_ = 'g'

simple_grid = [
    [_,_,_],
    [_,R,_],
    [_,_,_]
]
p = 1.0 / 9

initial_beliefs = [
    [1.0 / 9,1.0 / 9,1.0 / 9],
    [1.0 / 9,1.0 / 9,1.0 / 9],
    [1.0 / 9,1.0 / 9,1.0 / 9]
]

observation = R

expected_beliefs_after = [
    [1/11, 1/11, 1/11],
    [1/11, 3/11, 1/11],
    [1/11, 1/11, 1/11]
]

p_hit = 3.0
p_miss = 1.0

beliefs = []

for n in range(500):
    initial_beliefs = sense(observation, simple_grid, initial_beliefs, p_hit, p_miss)

print(initial_beliefs)
print(np.sum(initial_beliefs))