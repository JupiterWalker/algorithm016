# coding:utf-8
__author__ = 'cwang14'

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k%l
        self.reverse(nums, 0, l-k-1)
        self.reverse(nums, l-k, l-1)
        self.reverse(nums, 0, l-1)
        return nums

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1