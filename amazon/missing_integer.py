#Time O(n log(n))
def missing_int(A):
    max_value = max(A)
    # if all negatives return 1
    if max_value < 0:
        return 1



    #binary search with 0 as the search value
    A.append(0)
    s = sorted(A)
    zero_ind = 0
    low = 0
    high = len(s) - 1
    while low <= high:
        mid = (low + high) // 2
        if 0 == s[mid]:
            zero_ind = mid
        if 0 < s[mid]:
            high = mid - 1
        else:
            low = mid + 1
    s = s[zero_ind:]
    s = set(s)
    # search for missing positive integer
    for num in range(len(s)):
        if s.pop() != num:
            return num
    return max_value + 1


#A = [-100, -154, -2, -3, -4, 1, 3, 6, 4, 1, 2]
A = [-1, -2, 1,100]
print(missing_int(A))