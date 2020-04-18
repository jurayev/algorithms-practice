class Solution:
    """
    Time O(n/res) where res is output
    """
    def mySqrt(self, x):
        y = 0
        steps = 0
        while (y+1)**2 <= x:
            y += 1
            steps += 1
        print("Steps: %s" % steps)
        return y

    def sqrt_binary(self, x):
        """
        Time O(log(n))
        :param x: int
        :return: int
        """
        if 0 <= x <= 1:
            return x
        if 2 <= x <= 5:
            return x//2
        high = x // 3
        low = 0
        steps = 0
        while high >= low:
            mid = (high + low) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                high = mid - 1
            else:
                low = mid + 1
            steps += 1
        print("Steps: %s" % steps)
        return high
    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16


sol = Solution()

num = 10000000000000
print(num / 3162277)
print("Iterative:")
print(sol.mySqrt(num))
print("Binary:")
print(sol.sqrt_binary(num))
