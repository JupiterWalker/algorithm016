from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        res = []
        for i in range(l-3):
            if sum(nums[:4]) > target:
                break
            if (nums[i] + sum(nums[-3:])) < target:
                continue
            if i>0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, l-2):
                if nums[i] + sum(nums[j:j+3]) > target:
                    break
                if (nums[i] + nums[j] + sum(nums[-2:])) < target:
                    continue
                if j>(i+1) and nums[j-1] == nums[j]:
                    continue

                h, e = j+1, l-1
                while h<e:
                    s = nums[i] + nums[j] + nums[h] + nums[e]
                    if s == target:
                        res.append([nums[i],nums[j],nums[h],nums[e]])
                        e-=1
                        h+=1
                        while nums[e] == nums[e+1] and h<e:
                            e-=1
                        while nums[h] == nums[h-1] and h<e:
                            h+=1
                    elif s>target:
                        e-=1
                    else:
                        h+=1
        return res

if __name__ == '__main__':
    Solution().fourSum([1,0,-1,0,-2,2], 0)
