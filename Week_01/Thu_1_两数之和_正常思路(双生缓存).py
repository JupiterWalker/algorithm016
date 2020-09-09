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
        cache = {}
        for index, i in enumerate(nums):
            if (target - i) in cache:  # 2 他的另一个加数是否曾经遍历到过，被放在了缓存里
                return [cache[target-i], index]  # 3 在缓存里， 取出来一起返回
            cache[i] = index  # 1 我的另一半没有出现过，我把自己存在缓存里，等待我的加数来找我


if __name__ == '__main__':
    res = Solution().twoSum([1, 2, 3, 4, 5], 9)
    print(res)