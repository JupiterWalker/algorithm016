# coding:utf-8
__author__ = 'cwang14'

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        l = 0
        r = len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if mid > 0 and arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            elif mid > 0 and arr[mid - 1] < arr[mid] < arr[mid + 1]:
                l = mid
                print(f'l:{l}')
            elif mid > 0 and arr[mid - 1] > arr[mid] > arr[mid + 1]:
                r = mid
                print(f'r:{r}')
        return l


if __name__ == '__main__':
    test = [3, 5, 3, 2, 0]
    Solution().peakIndexInMountainArray(test)
