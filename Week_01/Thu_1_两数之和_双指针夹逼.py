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

# LCR 072. x 的平方根
# 给定一个非负整数 x ，计算并返回 x 的平方根，即实现 int sqrt(int x) 函数。
#
# 正数的平方根有两个，只输出其中的正数平方根。
#
# 如果平方根不是整数，输出只保留整数的部分，小数部分将被舍去。
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        ans = 0
        while r>=l:  # 两边不断夹逼，最终相遇一点，交插则代表结束

            mid = (l+r) //2
            if mid**2<=x:
                # 只有小于或等于目标值的 才会进来
                # 使得 ans 不断趋近 目标值
                ans = mid

                l = mid + 1  # 加减1为了处理左右边界相邻时，不会死循环，而会汇合于一点，比如：3,4
                             # ！！！ 二分法的二分结果包括边界， t=25: 3456 -> 56 - >55
            else:
                r = mid -1
        return ans