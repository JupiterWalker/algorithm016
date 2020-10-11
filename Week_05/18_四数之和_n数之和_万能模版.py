# coding:utf-8
__author__ = 'cwang14'

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        l = len(nums)

        def nSum(n, start, target, s, path):
            # 分治
            if n == 2:
                # 双指针夹逼
                left, right = start, l - 1
                while left < right:
                    _s = nums[left] + nums[right]
                    if _s == target:
                        res.append(path + [nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left, right = left + 1, right - 1
                    elif _s > target:
                        right -= 1
                    else:
                        left += 1
            else:
                # 在自己的区间内(start, l-(总-自己))遍历
                for index in range(start, l - n + 1):
                    # 枝剪
                    if nums[index] * n > target or nums[-1] * n < target:
                        return
                    # 去重
                    if index > start and nums[index - 1] == nums[index]:
                        continue
                    # 下一层
                    nSum(n - 1, index + 1, target - nums[index], s + nums[index],
                         path + [nums[index]])

        nSum(4, 0, target, 0, [])
        return res
