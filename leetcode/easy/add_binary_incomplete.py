class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        0 + 0 = 0
        0 + 1 = 1
        1 + 0 = 1
        1 + 1 = 10 (which is 0 carry 1)
        """
        diff = abs(len(a) - len(b))
        if len(a) > len(b):
           b = "0"*diff + b
        else:
           a = "0"*diff + a
        res = ""
        carry = "0"
        hmap = {"11": "10", "10": "1", "01": "1", "00": "0"}
        for i in range(1, len(a)+1):
            summ = hmap[a[-i]+b[-i]]
            res = hmap[summ[-1] + carry][-1] + res
            if hmap[summ[-1] + carry] == "10":
                carry = summ[0]
            else:
                carry = "0"
        if carry == "1":
            res = carry + res
        return res

sol = Solution()
a = "1111"
b = "1001"
exp = "11000"
print(sol.addBinary(a, b))
