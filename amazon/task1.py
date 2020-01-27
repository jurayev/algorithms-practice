# Time complexity O(n) - because we iterate linearly only once in each row for the given input
# Space compelxity O(1) - because we use only input 2d array, so the size is the same for any input
def numberAmazonGoStores(rows, column, grid):
    # count buildings
    buildings = 0
    for row in grid:
        for i in range(len(row)-1):
            if [row[i], row[i+1]] in [[0, 1], [1, 0]]:
                # reserve adjacent block to show that we have counted the building in this cluster already
                row[i+1] = 2
                # add up one more building
                buildings += 1
    return buildings
