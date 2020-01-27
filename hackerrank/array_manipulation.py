#!/bin/python3

import os

# Time complexity O(n*2) and Space complexity O(1)
def array_manipulation(n, queries):
    result = [0] * n
    for query in queries:
        for i in range(query[0] - 1, query[1]):
            result[i] += query[-1]
    return max(result)

n, queries = map(int, input().split())

arr = [0 for i in range(n+2)]
print(arr)

for i in range(queries):
    start, finish, k = map(int, input().split())
    arr[start - 1] += k
    arr[finish] -= k

ans = 0
current = 0
print(arr)
for i in arr:
    current += i
    if current > ans:
        ans = current

print(ans)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = array_manipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
