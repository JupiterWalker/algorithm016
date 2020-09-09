# coding:utf-8
__author__ = 'cwang14'


class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def helper(n) -> int:
            if n < 3:
                return n

            if n in cache:
                # 空降复杂度 O(n)的写法
                # return cache[n]

                # 每次n的缓存被击中，表示n+1的缓存已经生成，n+2的缓存将生成
                # n+1和n+2的缓存已经生成，并且以后不用再重新生成，所以n的缓存没有用了，可以扔掉了
                temp = cache[n]
                del cache[n]
                return temp
            else:
                res = helper(n - 1) + helper(n - 2)
                cache[n] = res
                return res

        return helper(n)


if __name__ == '__main__':
    #  时间复杂度 需要看最大递归的深度，最大递归为n， 所以时间复杂度为 O(n)
    #  空间复杂度为O(1)
    n = 10
    Solution().climbStairs(n)
