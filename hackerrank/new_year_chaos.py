# Time O(n) and space complexity O(1)
def minimum_bribes(n, q):
    bribes = 0
    for i in range(2):
        for r in reversed(range(1, n)):

            if q[r] < q[r-1]:
                q[r], q[r-1] = q[r-1], q[r]
                bribes += 1
        #1 2 3 4 5 6 7 8
        #2 5 1 3 4
        print(q)
        if q == sorted(q):
            return bribes
    return 'Too chaotic'

print(minimum_bribes(5, [2, 5, 3, 4, 1]))
