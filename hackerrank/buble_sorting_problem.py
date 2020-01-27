n = 5
a = [5, 2, 3, 1, 4]
counter = 0
# Time complexity O(n*2) and Space complexity O(1)
for i in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            counter += 1

print('Array is sorted in {0} swaps.'.format(counter))
print('First Element: {0}'.format(a[0]))
print('Last Element: {0}'.format(a[-1]))
print(a)
