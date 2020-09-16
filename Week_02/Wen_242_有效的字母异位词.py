# coding:utf-8
__author__ = 'cwang14'

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_dict = defaultdict(list)
        for string in strs:
            map_dict[tuple(sorted(string))].append(string)
        return list(map_dict.values())
