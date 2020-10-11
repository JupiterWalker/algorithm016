# coding:utf-8
__author__ = 'cwang14'

from collections import defaultdict
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset = set(wordList)
        if endWord not in wordset:
            return []
        _m, size = defaultdict(list), len(beginWord)
        begin_q, end_q, b2e = {beginWord}, {endWord}, True
        alpha = ''.join([chr(ord('a')+i) for i in range(26)])
        while begin_q:
            if len(begin_q) > len(end_q):
                begin_q, end_q, b2e = end_q, begin_q, not b2e
            print(wordset, begin_q)
            wordset -= begin_q
            _q = set()
            for word in begin_q:
                for i in range(size):
                    for l in alpha:
                        neighber = word[:i] + l + word[i+1:]
                        if neighber in wordset:
                            print('hit')
                            _q.add(neighber)
                            if b2e:
                                _m[neighber].append(word)
                            else:
                                _m[word].append(neighber)

            if _q & end_q:
                res = [[endWord]]
                while res[0][0] != beginWord:
                    res = [[x]+i for i in res for x in _m[i[0]]]
                return res

            begin_q = _q
        return []
