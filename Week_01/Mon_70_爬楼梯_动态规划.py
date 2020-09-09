# coding:utf-8
__author__ = 'cwang14'


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        two_before = 1
        one_before = 2

        for i in range(3, n+1):
            temp = one_before
            one_before = two_before + one_before
            two_before = temp

        return one_before


if __name__ == '__main__':
    #  时间复杂度为O(n)
    #  空间复杂度为O(1)
    n = 10
    Solution().climbStairs(n)