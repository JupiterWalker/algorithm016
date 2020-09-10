# coding:utf-8
__author__ = 'cwang14'


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack: self.stack.append((x, x))
        else:
            min = self.stack[-1][1]
            if x < min: self.stack.append((x, x))
            else: self.stack.append((x, min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack: return self.stack[-1][0]
        else: return

    def getMin(self) -> int:
        if self.stack: return self.stack[-1][1]
        else: return