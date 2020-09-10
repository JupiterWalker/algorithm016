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
        if not self.stack:
            self.min = x
            self.stack.append(x)
            print('初次上任%s'%x)
            return
        elif x <= self.min:  # 遇到更小的值
            self.stack.append(self.min-x)  # 先把差距推进栈，
            self.stack.append(x)  # 再把小值推进栈，
            self.min = x  # 登记现在的最小值，保证小值加上他下面的数就是之前的那个最小值
        else:  # 遇到大的值
            self.stack.append(x)  # 只是推进栈

    def pop(self) -> None:
        if self.min == self.stack[-1]:  # 如果现任的最小值卸任
            self.stack.pop()  # 卸任
            if not self.stack:  # 卸任后，无后继者
                self.min = None  # 最小值设None
                return
            self.min += self.stack.pop()  # 可以根据最小值加上他之后跟着的差距，自动算出下一任最小值
        else:
            self.stack.pop()  # 否则只是简单的出栈

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
