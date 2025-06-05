from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        h, t = 0, len(nums)-1
        for c in range(len(nums)):
            print(nums)
            if nums[c] ==1:
                continue

            while h<=c<=t and nums[c] in [0, 2]:
                if nums[c] == 0:
                    nums[c], nums[h] = nums[h], nums[c]
                    h+=1
                    print(nums)
                else:
                    nums[c], nums[t] = nums[t], nums[c]
                    t-=1
                    print(nums)
if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    Solution().sortColors(nums)
    print(nums)
