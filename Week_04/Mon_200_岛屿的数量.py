# coding:utf-8
__author__ = 'cwang14'

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def distory(row, col):
            if 0 <= row < self.l_row and 0 <= col < self.l_col and grid[row][col] == '1':
                grid[row][col] = '0'
                distory(row + 1, col)
                distory(row - 1, col)
                distory(row, col + 1)
                distory(row, col - 1)

        self.l_row = len(grid)
        self.l_col = len(grid[0])
        island_num = 0
        for row in range(self.l_row):
            for col in range(self.l_col):
                if grid[row][col] == '1':
                    island_num += 1
                    distory(row, col)
        return island_num
