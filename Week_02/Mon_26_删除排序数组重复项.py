# coding:utf-8
__author__ = 'cwang14'

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        slow_p = 0
        for fast_p in range(1, len(nums)):
            # 如果当前等于慢指针的， 快指针+1
            if nums[fast_p] == nums[slow_p]:
                pass
            # 如果当前不等于慢指针， 慢指针+1， 调换当前元素， 快指针+1
            else:
                slow_p += 1
                nums[slow_p] = nums[fast_p]
        return slow_p + 1
