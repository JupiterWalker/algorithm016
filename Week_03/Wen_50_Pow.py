# coding:utf-8
__author__ = 'cwang14'


class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(x, n):
            if n == 1:
                return x

            if n % 2 == 0:
                sub_r = self.myPow(x, n / 2)
                return sub_r * sub_r
            if n % 2 == 1:
                sub_r = self.myPow(x, (n - 1) / 2)
                return sub_r * sub_r * x

        if n == 0:
            return 1

        if n < 0:
            res = helper(x, -n)
            return 1 / res
        res = helper(x, n)
        return res
