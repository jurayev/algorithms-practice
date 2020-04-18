# Time O(log(n)) Space O(1)
def isPalindrome(x):
    x = str(x)
    mid = len(x) // 2
    for i in range(mid):
        left = x[i]
        right = x[-(i+1)]
        if left != right:
            return False
    return True

# Time O(1) Space O(1)
def isPalindrome1(x):
    x = str(x)
    length = len(x)
    if length == 1:
        return True
    mid = length // 2
    left = x[:mid]
    right = x[-mid:][::-1]
    if left == right:
        return True
    return False

# Time O(1) Space O(1)
def isPalindrome2(x):
    return str(x) == str(x)[::-1]


x = 11211
print(isPalindrome2(x))
