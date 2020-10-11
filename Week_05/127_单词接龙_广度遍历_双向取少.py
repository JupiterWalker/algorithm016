# coding:utf-8
__author__ = 'cwang14'

from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 如果天下无知己，则退出人生的游戏
        if endWord not in wordList:
            return 0
        # 制作地图,第一个一定会出自己的家乡并且不再回来，所以地图上不用加上第一个人的
        wordset = set(wordList)
        _m = defaultdict(list)
        size = len(beginWord)
        for word in wordset:
            for i in range(size):
                _m[word[:i]+'*'+word[i+1:]].append(word)

        # 正反序遍历记录记录自己身处的初始位置,以防重复走自己走过的路并且让对方知道自己之前是否来过
        begin_visited = defaultdict(bool)
        begin_visited[beginWord] = True
        end_visited = defaultdict(bool)
        end_visited[endWord] = True

        # 记录自己所处的城池链，方便知道下一次前进的方向
        begin_q = [beginWord]
        end_q = [endWord]
        step = 0
        # 如果任何一方找遍天下，没找到通往对方的路就放弃
        while begin_q:
            _q = deque()
            # 记录天数
            step += 1
            # 每天只能有一个人向下一城池链进发，所以找开销最小的
            if len(begin_q) > len(end_q):
                begin_q, begin_visited, end_q, end_visited = end_q, end_visited, begin_q, begin_visited
            # 对每个所在城池的可到达下个城市进行遍历
            for word in begin_q:
                for i in range(size):
                    for _similar in _m[word[:i]+'*'+word[i+1:]]:
                        # 如果发现知己在该城市，则结算之间的城市数=天数+1
                        if end_visited[_similar]:
                            return step + 1
                        # 记录自己到达过此地，方便一方下次知己行动，找到自己
                        if not begin_visited[_similar]:
                            begin_visited[_similar] = True
                            _q.append(_similar)

            begin_q = _q
        return 0