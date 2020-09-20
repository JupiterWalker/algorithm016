# coding:utf-8
__author__ = 'cwang14'

from collections import deque
from timeit import timeit
import dis
import  timeit
s = list(range(100000))
d = deque(s)

def dque_demo():
    a = d.pop()
    d.append(a)
    return

def dque_index_demo():
    a = d[777]
    return

def list_demo():
    a = s[777]
    return

# def dque_inset_demo():
#     d.insert(7, 666)
#     return
#
# def list_inset_demo():
#     s.insert(7, 666)
#     return

# print(f'dque pop append: {timeit.timeit(stmt=dque_demo)}')
print(f'dque[-1]: min{timeit.repeat(stmt=dque_index_demo, number=100)}')
print(f'list[-1]: {timeit.repeat(stmt=list_demo, number=100)}')
# print(f'dque insert: {timeit.repeat(stmt=dque_index_demo)}')
# print(f'list insert: {timeit.repeat(stmt=list_demo)}')