arrs = [
[1,1,1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 2, 4, 4, 0],
[0, 0, 0, 2, 0, 0],
[0, 0, 1, 2, 4, 0]
]
#for _ in range(6):
#        arrs.append(list(map(int, input().rstrip().split())))
sumHourGlass = 0
sumOfEachHourGlass = []
# Time complexity O(n*2) and Space complexity O(1)
for row in range(4):
    for column in range(4):
        for arr in range(row, 3 + row):
            for el in range(column, 3 + column):
                if arr == row + 1:
                    sumHourGlass += arrs[arr][el + 1]
                    break
                else:
                    sumHourGlass += arrs[arr][el]
        sumOfEachHourGlass.append(sumHourGlass)
        sumHourGlass = 0
print(max(sumOfEachHourGlass))
