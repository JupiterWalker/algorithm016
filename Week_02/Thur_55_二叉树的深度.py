# coding:utf-8
__author__ = 'cwang14'

#广度优先
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        queue = [root]
        while queue:
            next_layer_nodes = []
            for _root in queue:  # 把下一层的所有节点都收集起来
                if _root.left:
                    next_layer_nodes.append(_root.left)
                if _root.right:
                    next_layer_nodes.append(_root.right)
            res += 1
            queue = next_layer_nodes
        return res

#深度优先
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 找出子树们最大的一宗脉，本节点+1，作为一宗脉向上传递
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1