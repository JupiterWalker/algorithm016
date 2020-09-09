# coding:utf-8
__author__ = 'cwang14'

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(index, sum, path):
            if sum == target:
                res.append(path.copy())
                return 0
            if sum > target:
                return 0

            for i in range(index, len(candidates)):
                path.append(candidates[i])
                r = dfs(i, sum+candidates[i], path)
                path.pop()
                if r == 0:
                    return
        dfs(0, 0, [])
        return res


if __name__ == '__main__':
    res = Solution().combinationSum([1, 2, 3, 4], 8)
    print(res)