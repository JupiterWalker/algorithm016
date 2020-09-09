# coding:utf-8
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
#
#
#  示例:
#
#  给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(v, k) for k, v in enumerate(nums)]
        nums.sort()
        left, right = 0, len(nums)-1
        while left < right:
            s = nums[left][0] + nums[right][0]
            print(s)
            if s < target:
                while left < right and nums[left+1] == nums[left]:
                    left += 1
                left += 1
            elif s > target:
                while left < right and nums[right-1] == nums[right]:
                    right -= 1
                right -= 1
            else:
                return [nums[left][1], nums[right][1]]
        return []


if __name__ == '__main__':
    res = Solution().twoSum([1, 2, 3, 4, 5], 9)
    print(res)