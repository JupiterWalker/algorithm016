# coding:utf-8
__author__ = 'cwang14'

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        res = []
        for i in range(len(nums)):
            # 太子上台前要除掉比他弱的候选者
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            # 太子开始排队，前的都比他实力强，对立中的岁数一个比一个大
            q.append(i)
            # 死神每年看看队列靠前着到没到时候，到时候就带走
            if q[0] <= (i - k):
                q.pop(0)
            # 由队列最靠前也就是实力最强的这个登基
            if i >= k-1:
                res.append(nums[q[0]])
        # 返回历代皇帝
        return res