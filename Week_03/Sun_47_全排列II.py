# coding:utf-8
__author__ = 'cwang14'

# 初级版
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        _nums = list(enumerate(nums))
        res = []

        def helper(path):
            if len(path) == l:
                new = [i[1] for i in path]
                if new not in res:   # 在下一层拦截浪费开销
                    res.append(new)
                return

            for i, v in _nums:
                if (i, v) not in path:
                    helper(path + [(i, v)])

        helper([])
        return res


# 优化版


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        l, res = len(nums), []
        _nums = list(enumerate(nums))

        def helper(path):
            if len(path) == l:
                res.append([i[1] for i in path])
                return
            used = []  # 把非法的在上一层拦截，不要进入到下一层，浪费开销
            for i, v in _nums:
                if v in used: continue
                if (i, v) not in path:
                    used.append(v)
                    helper(path + [(i, v)])

        helper([])
        return res
