# coding:utf-8
__author__ = 'cwang14'


# DP
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l_row, l_col = len(text1), len(text2)
        cache = [[0] * (l_col + 1) for _ in range(l_row + 1)]
        for i in range(1, l_row + 1):
            for j in range(1, l_col + 1):
                if text1[i - 1] == text2[j - 1]:
                    cache[i][j] = cache[i - 1][j - 1] + 1
                else:
                    cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])
        return cache[-1][-1]


# 递归分治
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l_1, l_2 = len(text1), len(text2)
        cache = [[False] * l_2 for _ in range(l_1)]

        def helper(index_1, index_2):

            if index_1 == l_1 or index_2 == l_2:
                return 0

            if hit := cache[index_1][index_2]:
                return hit

            if text1[index_1] == text2[index_2]:
                cache[index_1][index_2] = helper(index_1 + 1, index_2 + 1) + 1
                return cache[index_1][index_2]
            else:
                cache[index_1][index_2] = max(helper(index_1 + 1, index_2),
                                              helper(index_1, index_2 + 1))
                return cache[index_1][index_2]

        return helper(0, 0)
