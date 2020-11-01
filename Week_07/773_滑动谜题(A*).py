# coding:utf-8
__author__ = 'cwang14'

from queue import PriorityQueue
from typing import List


class Solution:

    def Manhattan(self, s1, s2):
        '''估值函数'''
        dist = 0  # 所有元素距离他们应该在的位置的距离之和作为估值指标
        for i1, d in enumerate(s1):
            i2 = s2.index(d)
            dist += abs(i1 // 3 - i2 // 3) + abs(i1 % 3 + i2 % 3)
        return dist

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 向量模版
        # [0,1,2]
        # [3,4,5]
        v_map = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (3, 1, 5), (2, 4)]

        start_q = PriorityQueue()
        start_q.put((0, (''.join(str(e) for row in board for e in row), 0)))

        used = [''.join(str(e) for row in board for e in row)]
        while not start_q.empty():
            _, q = start_q.get()

            if q[0] == '123450': return q[1]

            zero_index = q[0].index('0')
            for index in v_map[zero_index]:
                _q, count = q[0][:], q[1]
                _q = list(_q)
                _q[zero_index], _q[index] = _q[index], _q[zero_index]
                _q = ''.join(_q)
                if _q not in used:
                    priority = self.Manhattan(_q, '123450')
                    # 放入结果和其估值（其估值需要考虑进之前走的步数）
                    start_q.put((count + 1 + priority, (_q, count + 1)))
                    used.append(_q)

        return -1
