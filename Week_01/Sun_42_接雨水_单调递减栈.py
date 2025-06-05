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

# 双指针获取当前扫过最大值
class Solution:
    def trap(self, height: List[int]) -> int:
        l_max, r_max = height[0], height[-1]
        l, r = 0, len(height)-1
        res = 0
        while l<r:
            if height[l] > height[r]:
                res += r_max - height[r]
                r -= 1
                r_max = max(r_max, height[r])
            else:
                res += l_max - height[l]
                l += 1
                l_max = max(l_max, height[l])
        return res