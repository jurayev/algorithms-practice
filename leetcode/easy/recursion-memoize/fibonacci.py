from decorators.profile import profile
# Time O(n). Space O(n)
class Solution1:

    # Time O(n). Space O(n)
    @profile
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        self.cache = {0: 0, 1: 1}
        return self.memoize(n)

    @profile
    def memoize(self, n):
        if n in self.cache.keys():
            return self.cache[n]
        self.cache[n] = self.memoize(n-1) + self.memoize(n-2)
        return self.memoize(n)

class Solution2:

    # Time O(2^n). Space O(n)
    @profile
    def fib(self, N: int) -> int:
        return N if N < 2 else self.fib(N - 1) + self.fib(N - 2)


class Solution3:

    # Time O(n). Space O(n)
    @profile
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.memoize(n)

    def memoize(self, n):
        cache = {0: 0, 1: 1}

        for i in range(2, n+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[n]


# Test cases
# 20 = 6765
# 40 = 102334155
sol1 = Solution1()
ans = sol1.fib(29)
print(f"Solution 2: {ans}")
print(f"Time elapsed: {sol1.memoize.__total_time__}")
print(f"N of calls: {sol1.memoize.__n_calls__}")

sol2 = Solution2()
ans2 = sol2.fib(29)
print(f"Solution 2: {ans2}")
print(f"Time elapsed: {sol2.fib.__total_time__}")
print(f"N of calls: {sol2.fib.__n_calls__}")

sol3 = Solution3()
ans3 = sol3.fib(29)
print(f"Solution 3: {ans3}")
print(f"Time elapsed: {sol3.fib.__total_time__}")
print(f"N of calls: {sol3.fib.__n_calls__}")
