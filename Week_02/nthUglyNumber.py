class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        丑数
        """
        res, i2, i3, i5 = [1] * n, 0, 0, 0
        for i in range(1, n):
            v2, v3, v5 = res[i2] * 2, res[i3] * 3, res[i5] * 5
            res[i] = min(v2, v3, v5)
            if res[i] == v2:
                i2 += 1
            if res[i] == v3:
                i3 += 1
            if res[i] == v5:
                i5 += 1
        return res[-1]