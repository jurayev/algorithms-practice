#O(n) space O(1)
def reverse(x):
    result = ""
    for i in reversed(str(x)):
        if i == "-":
            result = i + result
        else:
            result += i
    result = int(result)
    if (-2 ** 31) <= result <= (2 ** 31 - 1):
        return result
    return 0

x = 12340

print(reverse(x))