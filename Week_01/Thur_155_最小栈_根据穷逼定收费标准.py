# coding:utf-8
__author__ = 'cwang14'


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x: int) -> None:
        if self.min is None:
            self.min = x
            self.stack.append(0)
            return
        left_m = x - self.min
        self.stack.append(left_m)
        if left_m < 0:
            self.min = x
            return

    def pop(self) -> None:
        if self.stack:
            if len(self.stack) == 1:
                self.stack.pop()
                self.min = None
                return
            elif self.stack[-1] >= 0:
                self.stack.pop()
                return
            else:
                self.min = self.min - self.stack.pop()
                return

    def top(self) -> int:
        if self.stack:
            if self.stack[-1] >= 0:
                return self.stack[-1] + self.min
            else:
                return self.min

    def getMin(self) -> int:
        return self.min
