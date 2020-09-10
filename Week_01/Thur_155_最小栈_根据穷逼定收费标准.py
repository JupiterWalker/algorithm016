# coding:utf-8
__author__ = 'cwang14'


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.tax = None

    def push(self, x: int) -> None:
        if self.tax is None:
            self.tax = x  # 起初没有收保护费标准，第一个来，他要全部上交，并把他上交的额度最为保护费额度
        left_money = x-self.tax  # 上交后的积蓄,可能还欠着我们的
        if left_money < 0:  # 如果来了一个穷逼，没交够保护费，从此欠着我们的钱
            self.tax = x  # 感受到了大家好像比较穷，把穷逼的全部积蓄作为收保护费的标准
        self.stack.append(left_money)  # 带着剩下的钱正常生活

    def pop(self) -> None:
        if not self.stack:
            return
        if self.stack[-1] >= 0:  # 出来的这个交够了现在额度的保护费，返还之前收到的，可以放行
            return_money = self.stack.pop() + self.tax
            if len(self.stack) == 0:
                self.tax = None
            return return_money
        else:  # 因为他导致上次修改额度 成他积蓄的值
            temp_tax = self.tax  # 参考标准，返还你的积蓄
            self.tax = self.tax - self.stack.pop()  # 在他之前的收费标准
            return temp_tax # 带你所有的钱走吧

    def top(self) -> int:
        if self.stack:
            if self.stack[-1] > 0:
                return self.stack[-1] + self.tax  # 带着你现有的钱，再暂时返还你交过的税给你的家人看一眼，让他们放心安分一些
            else:
                return self.tax
        else:
            return

    def getMin(self) -> int:
        return self.tax   # 我们的最小值，就是我们收费的标准，因为它就是按照最小积蓄那个人而定的
