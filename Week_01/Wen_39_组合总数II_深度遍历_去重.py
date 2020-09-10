# coding:utf-8
__author__ = 'cwang14'

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()

        def helper(sum, path, nums):
            if sum > target:
                return 0
            if sum == target:
                res.append(path.copy())
                return 0

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                if i == len(nums):
                    return

                path.append(nums[i])
                r = helper(sum+nums[i], path, nums[i+1:])
                path.pop()
                if r == 0:
                    return
        helper(0, [], candidates)
        return res


if __name__ == '__main__':
    res = Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    print(res)