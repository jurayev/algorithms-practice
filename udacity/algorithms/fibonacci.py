# Time O(log(n)). Space O(1)
def get_fib(position):
    if position <= 0:
        return 0
    elif 1 <= position <= 2:
        return 1
    return get_fib(position - 1) + get_fib(position - 2)

# Test cases
print(get_fib(3))