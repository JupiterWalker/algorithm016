# coding:utf-8
__author__ = 'cwang14'

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                h = height[stack.pop()]
                if not stack:
                    break
                h = min(height[i], height[stack[-1]]) - h
                w = i - stack[-1] -1
                res += w*h

            stack.append(i)
        return res