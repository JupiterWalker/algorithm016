# coding:utf-8
__author__ = 'cwang14'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = [root]
        res.append([root.val])
        while q:
            next_layer = []
            for i in q:
                if i.left: next_layer.append(i.left)
                if i.right: next_layer.append(i.right)
            if next_layer:
                res.append([i.val for i in next_layer])
            q = next_layer
        return res