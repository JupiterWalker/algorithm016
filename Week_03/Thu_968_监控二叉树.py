# coding:utf-8
__author__ = 'cwang14'


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.res = 0

        def lrd(root):
            if not root:
                return 1

            left = lrd(root.left)
            right = lrd(root.right)

            # 分治, 回溯
            if left == 0 or right == 0:
                self.res += 1
                return 2
            elif left == 2 or right == 2:
                return 1
            else:
                return 0

        if lrd(root) == 0:
            self.res += 1
        return self.res
