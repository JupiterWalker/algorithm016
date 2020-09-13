# coding:utf-8
__author__ = 'cwang14'


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        max_area = 0
        for i in range(len(heights)):
            while stack and stack[-1][0] > heights[i]:
                bottom = i - stack[-2][1] - 1
                height = stack[-1][0]
                stack.pop()
                area = bottom * height
                max_area = max(max_area, area)
            stack.append([heights[i], i])
        return max_area
