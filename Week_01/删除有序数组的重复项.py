from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l_index, r_index = 1, len(nums) - 1
        last_num = nums[0]
        for i in range(1, len(nums) - 1):

            if i > 0 and nums[i] != last_num:
                last_num = nums[i]
                nums[i], nums[l_index] = nums[l_index], nums[i]
                l_index += 1
                if l_index == r_index:
                    return len(nums[:l_index])
                continue
            if i > 0 and nums[i] == last_num:
                last_num = nums[i]
                nums[i], nums[r_index] = nums[r_index], nums[i]
                r_index -= 1
                if l_index == r_index:
                    return len(nums[:r_index + 1])
                continue


if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    r = Solution().removeDuplicates(nums)
    print(r)