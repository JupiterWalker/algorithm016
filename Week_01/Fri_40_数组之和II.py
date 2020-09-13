# coding:utf-8
__author__ = 'cwang14'

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        res = []

        def helper(nums, sum, path):
            if sum > target:
                return 0
            if sum == target:
                res.append(path.copy())
                return 0

            for i in range(0, len(nums)):
                if i>0 and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                r = helper(nums[i+1:], nums[i]+sum, path)
                path.pop()
                if r == 0:
                    return
        helper(candidates, 0, [])
        return res