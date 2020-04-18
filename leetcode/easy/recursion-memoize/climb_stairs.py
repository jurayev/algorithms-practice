class Solution:
    # T: O(n) S: O(n)
    def climbStairs(self, n: int) -> int:
        # 1 -> 1 | 2 -> 2 | 3 -> 3 | 4 -> 5 | 5 -> 8|  6 -> 13 | 7 -> 21 | 8 -> 34 | 9->55
        # 1,1,1,1     1 1 1 1 1
        # 2,1,1       1 1 1 2
        # 1,2,1       1 1 2 1
        # 1,1,2       1 2 1 1
        # 2,2         2 1 1 1
        #             2 2 1
        #             2 1 2
        #             1 2 1

        if n <= 2:
            return n
        self.cache = {1: 1, 2: 2}
        return self.memoize(n)

    def memoize(self, n: int) -> int:
        if n in self.cache.keys():
            return self.cache[n]
        self.cache[n] = self.memoize(n - 1) + self.memoize(n - 2)
        return self.memoize(n)