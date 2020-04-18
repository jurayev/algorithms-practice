def solution(X, Y, A):
    N = len(A)
    result = -1
    nX = 0
    nY = 0
    for i in range(N):
        if A[i] == X:
            nX += 1
        elif A[i] == Y:
            nY += 1
        if nX == 1 and nY == 1:
            result = i
    #if nY + nX == 2:
    #    return N
    return result

X = 42
Y = 42
A = [73, 3, 2, 7, 42, 3, 7]

print(solution(X, Y, A))