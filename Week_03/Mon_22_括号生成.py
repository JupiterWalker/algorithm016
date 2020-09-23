# coding:utf-8
__author__ = 'cwang14'

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(left, right, path):
            if left == n and right == n:
                res.append(path)
                return
            if left <= n:
                dfs(left + 1, right, path + '(')
            if left > right:
                dfs(left, right + 1, path + ')')

        dfs(0, 0, '')
        return res
